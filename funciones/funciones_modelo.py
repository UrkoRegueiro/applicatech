################ Librerias ################
import pandas as pd
import numpy as np
import pickle
import json
import streamlit as st
from joblib import load
############################################################################################################
#################################### Función de carga de modelos ###########################################
@st.cache_resource
def load_model():
    min_model = load('modelos/min_model.pkl')
    max_model = load('modelos/max_model.pkl')

    lista_modelos = [min_model, max_model]

    return lista_modelos
############################################################################################################
#################################### Función de carga de lista de datos ####################################
def load_listas():

    with open("data/listas.json", 'r') as f:
        lista_datos = json.load(f)

    return lista_datos
############################################################################################################
#################################### Función carga encoders y scalers:######################################
def load_encoders():
    with open("encoders/jornada_encoder.pickle", 'rb') as file:
        encoder_jornada = pickle.load(file)

    with open("encoders/tipo_contrato_encoder.pickle", 'rb') as file:
        encoder_contrato = pickle.load(file)

    with open("encoders/comunidad_encoder.pickle", 'rb') as file:
        encoder_comunidad = pickle.load(file)

    with open("encoders/categoria_empleo_encoder.pickle", 'rb') as file:
        encoder_categoria = pickle.load(file)

    with open("encoders/tool_encoder.pickle", 'rb') as file:
        encoder_herramienta = pickle.load(file)

        lista_encoders = [encoder_jornada, encoder_contrato, encoder_comunidad, encoder_categoria, encoder_herramienta]

    return lista_encoders

def load_pca():
    with open("modelos/pca_min.pickle", 'rb') as file:
        pca_min = pickle.load(file)

    with open("modelos/pca_max.pickle", 'rb') as file:
        pca_max = pickle.load(file)

        lista_pca = [pca_min, pca_max]

    return lista_pca

############################################################################################################
#################################### Función de procesamiento de datos:#####################################
def data_transformer(X, lista_encoders, lista_pca):

    # Encoding a las columnas
    encoded_columns = ["jornada", "tipo_contrato", "comunidad", "categoria_empleo", "herramientas"]

    for columna, encoder in zip(encoded_columns, lista_encoders):

        if columna == "herramientas":
            data_encoded = encoder.transform(X[columna])
            df_encoded = pd.DataFrame(data_encoded, columns=encoder.classes_)
            X = pd.concat([X, df_encoded], axis=1).drop([columna], axis=1)

        else:
            data_encoded = encoder.transform(X[[columna]]).toarray()
            df_encoded = pd.DataFrame(data_encoded, columns=encoder.categories_)
            X = pd.concat([X, df_encoded], axis=1).drop([columna], axis=1)

    # Limpio nombre columnas
    X.columns = [str(columna).replace("('", "").replace("',)", "") for columna in X.columns]

    # Transformación PCA
    X_pca_min = lista_pca[0].transform(X)
    X_pca_max = lista_pca[1].transform(X)

    return X_pca_min, X_pca_max
############################################################################################################