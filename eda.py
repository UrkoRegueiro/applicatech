################ Funciones #################
import matplotlib.pyplot as plt
import streamlit
import streamlit_folium

from funciones.funciones_eda import *
############################################
def eda():
    st.markdown("""
        <style>
        .big-font {
            font-size:20px;
            color: #FAFAFA;
            
        }
        .sub-font {
            font-size:22px;
            color: #FAA227;
            font-weight: bold;                    
            
        }
        .center-font {
                font-size:25px;
                color: #FAA227;
                text-align: center;
            }
        </style>
        """, unsafe_allow_html=True)

                            #################### DATOS #####################

    _, df, df_comunidades, df_herramientas, provincias_geojson, _, _, _, _, _, df_grafico = load_data()

                            ################################################

    ####################################################  INTRODUCCIÓN ##########################################################################
    st.markdown("<h2 style='text-align: center; font-size: 60px;color: orange; '>Una visión general</h2>", unsafe_allow_html=True)

    st.markdown('<p class="center-font">¿Te has preguntado cuál es la situación actual de los empleos en el sector tecnológico español?<br></p>'
                '<p class="big-font">Reconocemos que las carreras en tecnología están entre las mejor remuneradas y con mejor biestar laboral, pero surge la duda sobre qué salario esperar cuando buscamos un empleo, ya sea tras graduarse o por una transición laboral. Aún más desafiante puede ser determinar qué habilidades específicas se requieren para destacar en este sector, y no digamos encontrar en qué empresa pueden encajar nuestros ideales.</p>'                
                '<p class="big-font">En nuestra búsqueda por despejar estas dudas, hemos recopilado información de los principales portales de empleo, analizándola para ayudarte a entender mejor el mercado tech en España. A continuación, te presentamos nuestros hallazgos para que estés un paso por delante en tu búsqueda de empleo.</p>', unsafe_allow_html=True)

    ################################################################## TABS ######################################################################

    tab1, tab2, tab3, tab4 = st.tabs([":orange[Distribución de empleos]"" :world_map:", ":orange[Salarios y Experiencia]"" :money_with_wings:", ":orange[Conocimientos]"" :gear:", ":orange[Empresas]"" :department_store:"])

    ###################################################### APARTADO DISTRIBUCION DE EMPLEOS ######################################################
    with tab1:
        st.markdown(" ")
        columna_texto_1, columna_mapa = st.columns((1, 1))

        with columna_texto_1:
            st.header(":orange[_Densidad de empleos Tech en España_]", divider="orange")
            # Descripción:
            st.markdown(
                '<p class="big-font">En el mapa de densidad situado a la derecha, se ofrece una visión general del número de empleos por comunidad autónoma. La realidad, aunque previsible, es que la mayor cantidad de ofertas de trabajo se concentran en Madrid y Cataluña. No obstante, es importante destacar que la actividad laboral en el sector tech se extiende más allá de estas áreas metropolitanas ya que, gracias a la flexibilidad del trabajo hídrido y remoto, se pueden desempeñar funciones para una posición desde cualquier lugar, disfrutando de un entorno laboral flexible.</p>',
                unsafe_allow_html=True)

        with columna_mapa:
            st.markdown(" ")
            st.markdown(" ")
            st.markdown(" ")
            st.markdown(" ")
            st.markdown(" ")
            st.markdown(" ")

            ################################################################
            ########## Densidad de empleos por comunidad autónoma ##########
            df_comunidad_suma = df.groupby('comunidad').size().reset_index(name='tot_jobs')
            df_comunidades = df_comunidades.merge(df_comunidad_suma, on='comunidad', how='left')
            df_comunidades["comunidad"] = df_comunidades["comunidad"].map(lambda x: re.sub(r'[áéíóúüàèìòùñ]', lambda m: unidecode(m.group()), str(x)))

            st.markdown(" ")
            mapa_españa = folium.Map(location=[40.223611, -1.979444], zoom_start=5)
            bins = np.arange(0, 7001, 500)
            legend_labels = [f"{i}-{i + 499}" for i in bins[:-1]]
            folium.Choropleth(
                                geo_data=provincias_geojson,
                                name="choropleth",
                                data=df_comunidades,
                                columns=["comunidad", "tot_jobs"],
                                key_on="properties.comunidad",
                                fill_color="RdYlBu_r",
                                bins=bins,
                                saturation=0.6,
                                fill_opacity=0.6,
                                line_opacity=.1,
                                legend_name="Número de empleos",
                                legend_labels=legend_labels).add_to(mapa_españa)

            folium.LayerControl().add_to(mapa_españa)
            folium_static(mapa_españa, width=600, height=410)

        ############################################################################################################
        st.divider()
        ############################################################################################################

        columna_categoria, columna_texto_2 = st.columns((1, 1))

        ###############################################
        ########## GRAFICO CATEGORIA TREEMAP ##########

        with columna_categoria:
            mask_cat = (df["categoria_empleo"] == "otros")
            df_titulos = df[~mask_cat].groupby(by="categoria_empleo")["titulo"].value_counts().to_frame().reset_index()
            df_titulos = df_titulos.groupby(by="categoria_empleo")[["categoria_empleo", "titulo", "count"]].head(3)

            min_size_cat = df_titulos['count'].min()
            max_size_cat = df_titulos['count'].max()
            df_titulos['normalized_size'] = np.interp(df_titulos['count'], (min_size_cat, max_size_cat), (10, 100))

            titulos = px.treemap(data_frame=df_titulos, values="count", path=["categoria_empleo", "titulo"],
                                 color="categoria_empleo",
                                 width=600,
                                 height=600,
                                 hover_data={"count": True, 'categoria_empleo': False, "normalized_size": False})

            titulos.update_layout(paper_bgcolor='rgb(17,17,17)', plot_bgcolor='rgb(17,17,17)', margin=dict(l=0, r=0, t=70, b=0))

            titulos.update_traces(marker=dict(cornerradius=5))

            st.plotly_chart(titulos, use_container_width=True)

        with columna_texto_2:

            st.header(":orange[_Empleos por categoría_]", divider="orange")
            st.markdown(
                '<p class="big-font">En el diagrama interactivo de la izquierda podemos apreciar la distribución y densidad de empleos por categoría en el sector tecnológico.Es importante señalar que, si bien la representación gráfica no refleja exactamente el tamaño real del mercado laboral de cada especialidad, existe una relación directa: a mayor área que ocupa una categoría en el diagrama, mayor es el número de oportunidades laborales disponibles.<br>'
                'Por ejemplo, la categoría de "programador", que incluye puestos como "developer" y "software engineer", es especialmente prominente, lo que nos indica una mayor demanda de este perfíl, sugiriendo que es altamente demandado debido a la versatilidad de sus funciones.</p>',
                unsafe_allow_html=True)





    ###################################################### APARTADO SALARIO Y EXPERIENCIA ######################################################
    with tab2:
        st.markdown(" ")
        columna_texto_3, columna_salario = st.columns((1, 1))

        with columna_texto_3:
            st.header(":orange[_Distribución de salarios Tech_]", divider="orange")
            # Descripción:
            st.markdown(
                '<p class="big-font">En el histograma de la derecha podemos observar la distribución de los salarios en el sector tecnológico español, donde la media se sitúa en los 35.800€ brutos anuales.<br>'
                'Del gráfico se distinguen los salarios mínimos en un rango que va de los 18.000€ a los 25.000€, mientras que los máximos van de los 50.000€ en adelante, presentando una distribución más amplia y la posibilidad de acceder a una gama de salarios máximos potenciales a mayor experiencia laboral adquirida.<br>'
                'Este tipo de gráfico nos ayuda a entender rápidamente la variabilidad de los salarios dentro de un campo específico, pudiendo identificar tanto los niveles de entrada como los salarios más altos en el mercado tech.</p>',
                unsafe_allow_html=True)

        with columna_salario:
            ######################################################
            ########## Distribucion de salarios ##################

            df_salarios = df.dropna(subset=['salario_min', 'salario_max'], how='all')
            df_salarios = df_salarios[df_salarios['salario_min'] > 15000]
            df_salarios = metodo_tukey(df_salarios, 'salario_min', 1.5)
            df_salarios = metodo_tukey(df_salarios, 'salario_max', 1.5)

            grafico_salarios = px.histogram(data_frame=df_salarios,
                                            x=["salario_min", "salario_max"],
                                            nbins=30,
                                            marginal="box",
                                            color_discrete_map={"salario_min": "#66B78D", "salario_max": "#FFBD45"})

            grafico_salarios.update_layout(legend= dict(x=0.7, y= 0.6, font=dict(size=16)),
                                           xaxis_title="Salario",
                                           yaxis_title="Frecuencia",
                                           font=dict(family="Courier New, monospace", size=42, color="#000000"),
                                           paper_bgcolor='rgb(17,17,17)',
                                           plot_bgcolor='rgb(17,17,17)',
                                           height=600, width=650,
                                           margin=dict(l=0, r=0, t=75, b=0))

            grafico_salarios.update_traces(name="Salario mínimo", selector=dict(name="salario_min"))
            grafico_salarios.update_traces(name="Salario máximo", selector=dict(name="salario_max"))
            st.plotly_chart(grafico_salarios, use_container_width=True)

        ############################################################################################################
        st.divider()
        ############################################################################################################

        columna_experiencia, columna_texto_4 = st.columns((1, 1))

        with columna_texto_4:
            st.header(":orange[_Demanda de experiencia_]", divider="orange")
            st.markdown(
                '<p class="big-font">En cuanto a la experiencia laboral demandada, del gráfico extraemos que este mercado demanda a una gran cantidad de trabajadores con experiencia de entre 2 y 3 años, revelando una dificultad de acceso a perfiles junior o recién graduados.<br>'
                'Por otra parte se observa que el resto de puestos ofertados requieren una experiencia de 4 años o más, habiéndo casos particulares con una demanda de experiencia especifica.</p>',
                unsafe_allow_html=True)


        with columna_experiencia:
            ######################################################
            ########## Distribución de experiencia ###############
            df_experiencia = df["experiencia"].value_counts().sort_index().to_frame().reset_index()

            grafico_experiencia = go.Figure(data=[go.Bar(
                x=df_experiencia['experiencia'], y=df_experiencia['count'],
                text=df_experiencia['experiencia'],
                textposition='auto',
                marker={"color": list(range(0, len(df_experiencia['experiencia']))), 'colorscale': 'blugrn'})])

            grafico_experiencia.update_layout(barmode='stack',
                                              xaxis_type='category',xaxis_tickvals=[0],
                                              xaxis_ticktext= [" "],
                                              xaxis_title="Años de experiencia",
                                              yaxis_title="Número de empleos",
                                              paper_bgcolor='rgb(17,17,17)',
                                              plot_bgcolor='rgb(17,17,17)',
                                              font=dict(family="Courier New, monospace",size=42,color="#000000"),
                                              width=650,
                                              height=450,
                                              margin=dict(l=0, r=0, t=70, b=0),
                                              autosize=True)

            grafico_experiencia.update_traces(textfont=dict(color='#FF7300'))
            st.plotly_chart(grafico_experiencia, use_container_width=True)

    ###################################################### APARTADO CONOCIMIENTOS ######################################################

    with tab3:
        st.markdown(" ")
        columna_texto_5, columna_stack = st.columns((1.2, 3))

        with columna_texto_5:
            st.header(":orange[_Stack Tecnológico_]", divider="orange")
            # Descripción:
            st.markdown(
                '<p class="big-font">Sin lugar a dudas observamos en el gráfico que el conocimiento con mayor demanda en este sector es el inglés, ya que gran parte de las empresas tecnológicas operan a nivel internacional.<br>'
                'Por otra parte le siguen los conocimientos en Microsoft 365 y el leguaje de consultas a bases de datos SQL, dos herramientas muy necesarias en este sector donde los datos son los cimientos.<br>'
                'Finalmente, dependiendo de la categoría de empleo, tendremos diferente demanda de conocimientos. Por ejemplo, como veremos, en programación se demanda en su mayor parte conocimientos de Java, mientras que en Data Driven se requiere Python.</p>',
                unsafe_allow_html=True)

        with columna_stack:
            ######################################################
            ########## GRAFICO HERRAMIENTAS TOP ESPAÑA ###########
            st.markdown(" ")
            st.markdown(" ")
            st.markdown(" ")

            boton_left, boton_right = st.columns((4,1))

            if boton_right.toggle(label=":orange[Sin Inglés]", help="Activalo para visualizar sin el inglés."):
                mask = df_herramientas["herramienta"] == "ingles"
                top_30_herramientas = df_herramientas[~mask].sort_values(by="count", ascending=False).head(30)

            else:
                top_30_herramientas = df_herramientas.sort_values(by="count", ascending= False).head(30)

            grafico_herramientas = go.Figure(data=[go.Bar(
                                                         x= top_30_herramientas['herramienta'], y= top_30_herramientas['count'],
                                                         text= top_30_herramientas['herramienta'],
                                                         textposition='auto',
                                                         marker={"color": list(range(0, len(top_30_herramientas['herramienta']))), 'colorscale': 'blugrn'})])

            grafico_herramientas.update_layout(
                                                barmode='stack',
                                                xaxis_type='category',
                                                xaxis_tickvals=[0],
                                                xaxis_ticktext= [" "],
                                                paper_bgcolor='rgb(17,17,17)',
                                                plot_bgcolor='rgb(17,17,17)',
                                                font=dict(family="Courier New, monospace",size=40,color="#000000"),
                                                height=600,
                                                margin=dict(l=0, r=0, t=0, b=0))


            st.plotly_chart(grafico_herramientas, use_container_width=True)

        ############################################################################################################
        st.divider()
        ############################################################################################################

        columna_stack_salario, columna_texto_6 = st.columns((2, 1.2))

        with columna_texto_6:
            st.header(":orange[_Salario según Stack_]", divider="orange")
            st.markdown(
                '<p class="big-font">En la gráfica de la izquieda se muestra la distribución del salario medio de cada una de las 20 herramientas más demandadas (sin tener en cuenta el inglés), revelando que Amazon Web Services es la mejor pagada, siendo el salario medio de 42.000€, siguiendole Azure, Scrum y Docker con 39.000€ de media.<br>'
                'En tabla inferior se exponen los salarios medios de cada una de las 20 herramientas, de mayor a menor:</p>',
                unsafe_allow_html=True)

            herramientas_salario = df_grafico.groupby("herramienta")["salario_medio"].mean().sort_values(ascending=False).to_frame().reset_index()
            herramientas_salario["salario_medio"] = herramientas_salario["salario_medio"].apply( lambda x: str(round(int(x), -3)) + " €")

            st.markdown(" ")
            st.markdown(" ")

            tabla = go.Figure(data=[go.Table(
                header=dict(values=['Herramienta', 'Salario medio'],
                            line_color='#66B78D',
                            fill_color='#66B78D',
                            align='center'),
                            cells=dict(values=[herramientas_salario["herramienta"].values, herramientas_salario["salario_medio"].values],
                            height=30,
                            line_color='#66B78D',
                            fill_color='#111111',
                            align='center'))])

            tabla.update_layout(width=450,
                                height=148,
                                font=dict(color="white", size=20),
                                paper_bgcolor='rgb(17,17,17)',
                                plot_bgcolor='rgb(17,17,17)',
                                margin=dict(l=5, r=100, t=0, b=0))
            st.plotly_chart(tabla, use_container_width=True)

        with columna_stack_salario:

            ##################################################
            ########## GRAFICO SALARIO-HERRAMIENTA ###########
            st.markdown(" ")
            st.markdown(" ")

            joy_grafica, ax = joypy.joyplot(
                data=df_grafico,
                by='herramienta',
                column='salario_medio',
                colormap=sns.color_palette("viridis", as_cmap=True),
                alpha=0.7,
                linewidth=1,
                figsize=(11, 7),
                background="#111111",
                linecolor="white"
                )
            for a in ax:
                label = a.get_yticklabels()
                a.set_yticklabels(label, fontdict={'color': 'white'})


            # Configuraciones adicionales
            plt.axvline(x=20000, color="white")
            plt.axvline(x=30000, color="white")
            plt.axvline(x=40000, color="white")
            plt.axvline(x=50000, color="white")
            plt.axvline(x=60000, color="white")
            plt.xticks(np.arange(10_000, 100_000, 10_000), color="white")
            plt.xlabel("Salario medio", color="white", size=15)
            plt.tick_params(axis="x", colors="white")
            joy_grafica.set_facecolor("#111111")
            st.pyplot(joy_grafica, use_container_width=True)

    ###################################################### APARTADO EMPRESAS ######################################################

    with tab4:
        st.markdown(" ")
        columna_texto_7, columna_empresas = st.columns((1, 3))

        with columna_texto_7:
            st.header(":orange[_Ofertas publicadas por empresa_]", divider="orange")
            # Descripción:
            st.markdown(
                '<p class="big-font">Lorem ipsum dolLorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempLorem ipsum dolor sit amet, consectetLorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempLorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempLorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempLorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempur adipiscing elit, sed do eiusmod tempLorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.</p>',
                unsafe_allow_html=True)

        with columna_empresas:
            #############################################################
            ########## empresa con número de puestos ofertados ##########

            df_empresas = df.copy()
            top_15_empresas = df_empresas['empresa'].value_counts().head(25)
            df_empresas_top_15 = df_empresas[df_empresas['empresa'].isin(top_15_empresas.index)]
            df_empresas_top_15['total'] = 1
            mask_empleo = df_empresas_top_15['categoria_empleo'] != 'otros'

            graf_empresas_top = px.treemap(df_empresas_top_15[mask_empleo],
                             values="total",
                             path=["empresa", "categoria_empleo"],
                             hover_name="categoria_empleo",
                             color_discrete_map={'red': 'red', 'blue': 'blue', 'green': 'green'})

            graf_empresas_top.update_traces(marker=dict(cornerradius=5))
            graf_empresas_top.update_layout(paper_bgcolor='rgb(17,17,17)', plot_bgcolor='rgb(17,17,17)',
                                            width=1000,
                                            height=600,
                                            margin=dict(l=0, r=0, t=115, b=0))

            st.plotly_chart(graf_empresas_top, use_container_width=True)

        ############################################################################################################
        st.divider()
        ############################################################################################################

        columna_beneficios, columna_texto_8 = st.columns((2, 1))

        with columna_texto_8:
            st.header(":orange[_¿Ofrecen beneficios?_]", divider="orange")
            st.markdown('<p class="big-font">Lorem ipsum dolLorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempLorem ipsum dolor sit amet, consectetLorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempLorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempLorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempLorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempur adipiscing elit, sed do eiusmod tempLorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.</p>',
                unsafe_allow_html=True)

        with columna_beneficios:
            ########## Porcentaje de empleos con beneficios #############
            #############################################################

            df_beneficios = (df["beneficios"].value_counts(normalize=True) * 100).reset_index()
            df_beneficios["proportion"] = df_beneficios["proportion"].apply(lambda x: round(x))
            df_beneficios.loc[0, "beneficios"] = f" <br><br><br><br><br> No ofrecen"
            df_beneficios.loc[1, "beneficios"] = f" <br>Sí ofrecen"
            text = [f'{valor}<br>{p}% <br> ' for p, valor in zip(df_beneficios['proportion'], df_beneficios['beneficios'])]

            grafico_beneficios = go.Figure(data=[go.Bar(
                                                        x=df_beneficios['beneficios'],
                                                        y=df_beneficios['proportion'],
                                                        text=df_beneficios['beneficios'],
                                                        textposition='inside',
                                                        textfont=dict(color='black'),
                                                        marker={"color": list(range(0,len(df_beneficios['beneficios']))),'colorscale':  [[0, '#66B78D'],[1, '#2A7271']]})])

            grafico_beneficios.update_layout(barmode='stack',
                                             xaxis_type='category',
                                             xaxis_tickvals=[0],
                                             xaxis_ticktext= [" "],
                                             xaxis_title="Beneficios",
                                             paper_bgcolor='rgb(17,17,17)',
                                             plot_bgcolor='rgb(17,17,17)',
                                             font=dict(family="Courier New, monospace",size=40,color="#000000"),
                                             width=800,
                                             height=600,
                                             margin=dict(l=0, r=0, t=64, b=0))

            grafico_beneficios.update_traces(text=text,
                                             texttemplate='%{text}',
                                             textfont=dict(color='white', size=30))

            st.plotly_chart(grafico_beneficios, use_container_width=True)