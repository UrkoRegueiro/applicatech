################ Funciones #################
import streamlit

from funciones.funciones_eda import *

############################################

def compara():
    st.markdown("""
            <style>
            .big-font {
                font-size:20px;
                color: #FFFFFF;

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

    st.markdown("""
        <style>

        	.stTabs [data-baseweb="tab-list"] {
        		gap: 5px;

            }

        	.stTabs [data-baseweb="tab"] {
        		height: 60px;
        		width: auto;
                white-space: pre-wrap;
        		background-color: #111111;
        		border-radius: 3px 3px 0px 0px;
        		gap: 1px;
        		padding-top: 10px;
        		padding-bottom: 1px;
        		padding-right: 25px;
            }

            .stTabs [data-baseweb="tab-list"] button [data-testid="stMarkdownContainer"] p {
        font-size:1.25rem;
        }

            .st-cn {
    background-color: orange;
    }

        	.stTabs [aria-selected="true"] {
          		background-color: #111111;
        	}

        </style>""", unsafe_allow_html=True)

                                    ##################### DATOS ####################

    _, df, _, df_herramientas, _, df_spider, df_spider_sin_ingles, df_salarios, df_salario_medio, df_stack, _ = load_data()

                                    ################################################

    ####################################################  INTRODUCCIÓN ##########################################################################

    st.markdown("<h2 style='text-align: center; font-size: 60px;color: orange; '>Investiga al detalle cada rincón</h2>", unsafe_allow_html=True)

    st.markdown(
        '<p class="center-font">¿Tienes dudas más específicas sobre el mercado laboral tech en España?<br></p>'
        '<p class="big-font">En tu búsqueda de comprender a fondo el mercado laboral tecnológico en España, entendemos que las preguntas pueden volverse más concretas y detalladas. ¿Qué combinación de habilidades tecnológicas se ajustan más a cada sector particular? ¿O quizás estás intrigado por la distribución salarial en distintas comunidades autónomas?</p>'
        '<p class="big-font">En esta sección, te invitamos a explorar el mercado tech español minuciosamente, dónde podrás personalizar y comparar datos específicos según tus necesidades, a través de herramientas visuales interactivas para que tengas un mejor entendimiento de la situación actual.</p>',
        unsafe_allow_html=True)

    ################################################################## TABS ######################################################################

    tab1, tab2, tab3 = st.tabs([":orange[Un vistazo al Stack Tecnológico]"":open_book:", ":orange[Salario por comunidad]"":heavy_dollar_sign:", ":orange[Rangos]"":abacus:"])

    ###################################################### APARTADO STACK TECNOLOGICO ######################################################
    with (tab1):

        columna_texto_1, columna_funnel_sun,  = st.columns((1, 2))

        with columna_texto_1:
            st.header(":orange[_Salario y Modalidad_]", divider="orange", help="Gráfico interactivo")
            st.markdown(
                '<p class="big-font">Conocer la banda salarial en la que se mueven la mayoría de empleos dentro cada uno de los sectores tecnológicos es interesante para ubicar en dónde se encuentran los roles mejor remunerados. Como podemos observar en la gráfica superior, los profesionales enmarcados como ML Engineer tienen un salario notablemente mayor al del resto de sectores, lo que con casi total probabilidad se deba a que la cantidad de datos recabados de ofertas en este área es muy inferior al resto. Por otro lado, si nos fijamos en los empleos que se encuentran en la parte inferior de la pirámide vemos que el salario mínimo medio supera al SMI (15.876€) en un 60%.<br>'
                '<br>'
                'Otro de los factores a tener en cuenta es la modalidad, pudiendo ser presencial, híbrida o remota. En la gráfica inferior es claramente visible que la mayoría de empresas de todos los sectores no consideran imprescindible que los trabajadores se desplacen físicamente a sus oficinas, siendo el trabajo remoto la opción mayoritaria. En cuanto a los trabajos que precisan presencialidad, se puede observar que hay mucha diferencia entre el número de ofertas con un formato híbrido en comparación con la presencialidad total, siendo esta última la que aparece en menor medida.</p>',
                unsafe_allow_html=True)

        with columna_funnel_sun:
            ############################################################
            ###################### GRAFICO FUNNEL ######################
            color_funnel = {"Salario Medio Minimo": "#66B78D", "Salario Medio Maximo": "#FFBD45"}

            salarios_comp = px.funnel(df_salarios,
                                      x='salario',
                                      y='categoria_empleo',
                                      color="tipo",
                                      color_discrete_map=color_funnel)

            salarios_comp.update_traces(texttemplate="%{value:,d} €")
            salarios_comp.update_layout(paper_bgcolor='rgb(17,17,17)',
                                        plot_bgcolor='rgb(17,17,17)',
                                        yaxis_title="",
                                        font=dict(family="Courier New, monospace", size=15, color="#000000"),
                                        legend=dict(x=0.3, y= 1.4, font=dict(size=18)),
                                        height = 450,
                                        margin = dict(l=0, r=0, t=180, b=0))
            st.plotly_chart(salarios_comp, use_container_width=True)

            ############################################################
            ###################### GRAFICO PRESENCIALIDAD ##############
            color_sunburst = {"presencial": '#C4E6C3', "hibrido": '#66B78D', "remoto": '#2A7271'}
            # "#C4E6C3" "#66B78D"  # 2A7271"

            mask_presencialidad = (df["presencialidad"] != "no especificado") & (df["categoria_empleo"] != "otros")
            df_presencialidad = df[mask_presencialidad].groupby(by="presencialidad")[
                "categoria_empleo"].value_counts().reset_index()

            grafico_presencialidad = px.sunburst(df_presencialidad,
                                                 path=['presencialidad', 'categoria_empleo'],
                                                 values='count',
                                                 color="presencialidad",
                                                 color_discrete_map=color_sunburst)
            grafico_presencialidad.update_layout(paper_bgcolor='rgb(17,17,17)',
                                                 plot_bgcolor='rgb(17,17,17)',
                                                 font=dict(family="Courier New, monospace", size=18, color="#000000"),
                                                 height = 450,
                                                 margin = dict(l=120, r=0, t=70, b=0))

            st.plotly_chart(grafico_presencialidad, use_container_width=True)

        ############################################################################################################
        st.divider()
        ############################################################################################################

        st.header(":orange[_Stack Tecnológico_]", divider="orange", help="Gráfico interactivo")
        st.markdown(
            '<p class="big-font">Dependiendo del sector se utilizarán diferentes herramientas para llevar a cabo tareas específicas, por ello se puede observar como, auque haya herramientas comunes, el stack más utilizado cambiará dependiendo de la categoría. Cabe destacar que el inglés, como conocimiento transversal, es muy demandado en la mayoría de empleos. Finalmente los servicios de computación en la nube como Amazon Web Services o Microsoft Azure también se solicitan de forma recurrente.<br><br>'
            'En el gráfico interactivo inferior podrás explorar más detenidamente el stack de cada una de las diferentes categorías:</p>',
            unsafe_allow_html=True)

        herr_1, herr_2, herr_3 = st.columns((0.1, 1, 4))
        herr_2.markdown(" ")
        boton_ingles = herr_2.toggle(label=":orange[Sin Inglés]", help="El filtrado se aplicará a toda la página.")
        herr_2.markdown(" ")
        herr_2.markdown(" ")
        herr_2.markdown(" ")
        herr_2.markdown(" ")

        categorias = df_stack.columns[1:]

        boton = herr_2.radio("Escoge la categoría", categorias)

        if boton:
            if boton_ingles:
                mask_ingles = (df_stack["herramienta"] != "ingles")
                df_stack = df_stack[mask_ingles]

            df_categoria = df_stack[[boton, "herramienta"]].sort_values(by=boton, ascending=False).head(20)

            grafico_stack = go.Figure(data=[go.Bar(
                x=df_categoria['herramienta'], y=df_categoria[boton],
                text=df_categoria['herramienta'],
                textposition='auto',
                marker={"color": list(range(0, len(df_categoria['herramienta']))), 'colorscale': 'blugrn'})])

            grafico_stack.update_layout(barmode='stack', xaxis_type='category', xaxis_tickvals=[0],
                                        xaxis_ticktext=[" "],
                                        #yaxis_ticklabel=
                                        title=f'<b></b><b>Stack tecnológico de {boton}</b>',
                                        paper_bgcolor='rgb(17,17,17)',
                                        plot_bgcolor='rgb(17,17,17)',
                                        font=dict(family="Courier New, monospace", size=40, color="#000000"),
                                        width=1000, height=400, margin=dict(l=0, r=0, t=70, b=0),
                                        autosize=True)
            herr_3.plotly_chart(grafico_stack, use_container_width=True)

        ################### GRAFICO SPIDER ##########################
        #############################################################
        columna_texto_2, columna_spider = st.columns((1, 2))
        with columna_texto_2:
            st.header(":orange[_Compara herramientas_]", divider="orange")
            st.markdown(
                '<p class="big-font">La diversidad de herramientas disponibles en la actualidad es asombrosa, abarcando una amplia gama de funciones y aplicaciones en diversos campos. La complejidad y la constante evolución de la tecnología pueden dificultar la tarea de identificar en qué sectores específicos estas herramientas encuentran su máxima utilidad. Con el objetivo de facilitar este proceso, hemos desarrollado una gráfica interactiva que permite seleccionar entre la extensa lista de herramientas disponibles en nuestra base de datos. Así, se proporciona una visión clara de la demanda en diferentes sectores, ayudando a los profesionales a tomar decisiones informadas sobre qué herramientas son más relevantes para sus necesidades y en qué industrias se solicitan con mayor frecuencia.</p>',
                unsafe_allow_html=True)

        with columna_spider:



            if boton_ingles:
                df_spider = df_spider_sin_ingles

            eleccion = st.multiselect(label="",
                                       options=df_spider["herramienta"],
                                       default=["python", "java", "sql"],
                                       max_selections=3)

            spider_izq, spider_drch = st.columns((1, 4))

            categories = df_spider.columns[:-1]
            N = len(categories)

            # Ángulos
            angles = [(n / float(N) * 2 * pi) for n in range(N)]
            angles += angles[:1]

            spider, ax = plt.subplots(figsize=(10, 10), subplot_kw={'projection': 'polar'}, facecolor='#111111')

            ax.set_theta_offset(pi / 2)
            ax.set_theta_direction(-1)
            plt.xticks(angles[:-1], categories, color="#FF7300", size= 20, ha="center")
            ax.set_xticks(angles[:-1])

            ax.set_rlabel_position(-30)
            plt.yticks([0, 0.25, 0.5, 0.75, 1], ["0%","25%", "50%", "75%", "100%"], color="#FFFFFF", size=18, va="bottom", ha="right")
            ax.grid(color="#FFFFFF")
            ax.set_facecolor("#111111")
            for spine in ax.spines.values():
                spine.set_edgecolor('#FFFFFF')
            plt.ylim(0, 1)

            for herramienta in eleccion:
                values = df_spider[df_spider["herramienta"] == herramienta].drop(['herramienta'], axis=1).values.flatten().tolist()
                values += values[:1]  # Close the plot
                label = herramienta  # Use ferramenta directly for label
                ax.plot(angles, values, linewidth=4, linestyle='solid')
                ax.fill(angles, values, alpha=0.3, label=label)  # Use viridis colormap for better distinction

            plt.legend(bbox_to_anchor=(1.31, 1.05), fontsize= 15, facecolor= "#111111", edgecolor= "#FFFFFF", labelcolor="#FF7300")
            spider_drch.pyplot(spider, use_container_width=True)

    ###################################################### APARTADO GEOGRAFIA ######################################################
    with tab2:
        st.header(":orange[_Salarios_]", divider="orange")
        st.markdown(
            '<p class="big-font">El salario de un trabajador está estrechamente vinculado a la ubicación geográfica en la que desempeña su empleo, reflejando la necesidad de que sea coherente con el costo de vida local. Para abordar esta variable, hemos creado gráficos interactivos que ofrecen una visión detallada de la distribución salarial en las diferentes comunidades autónomas, permitiendo comparaciones directas entre dos regiones simultáneamente. Estos gráficos son herramientas con las que comprender las disparidades salariales y facilitar decisiones informadas tanto a trabajadores en busca de empleo como a empresas que diseñan estrategias salariales adaptadas a las características específicas de cada localidad.</p>',
            unsafe_allow_html=True)


        ################### GRAFICO SALARIO MEDIO ###################
        #############################################################
        izq, centro, drcha = st.columns((2, 1.5, 2))
        st.info(":red[Nota:] En algunas comunidades la falta de datos provoca que la distribución de densidad no se ajuste correctamente.")
        columna_salario, columna_indicador = st.columns((4, 2))

        comunidades = ["", ""]
        valores = [0, 0]

        eleccion_comunidad = centro.multiselect(label="Comunidades Autónomas",
                                              options=df_salario_medio["comunidad"],
                                              default=["Galicia", "Comunidad de Madrid"],
                                              max_selections=2)




        with columna_salario:

            ################### GRAFICO COMPARADOR ###################
            ##########################################################
            df_salario_comunidad = df[df["pais"] == "España"][["comunidad", "salario_min", "salario_max"]].dropna()
            df_salario_comunidad = metodo_tukey(df_salario_comunidad, "salario_min", 1.5)
            df_salario_comunidad = metodo_tukey(df_salario_comunidad, "salario_max", 1.5)
            df_salario_comunidad["salario_medio"] = (df_salario_comunidad["salario_min"] + df_salario_comunidad["salario_max"]) / 2
            max_salario = int(df_salario_comunidad["salario_medio"].max()) + 1000
            min_salario = int(df_salario_comunidad["salario_medio"].min()) - 900

            mi_paleta = sns.color_palette("tab20", 20)
            comunidad_color_dict = {comunidad: color for comunidad, color in
                                    zip(df_salario_comunidad['comunidad'].unique(),
                                        sns.color_palette(mi_paleta, len(df_salario_comunidad['comunidad'].unique())))}

            if len(eleccion_comunidad) >= 1:
                comunidades[0] = eleccion_comunidad[0]
                valores[0] = df_salario_medio[df_salario_medio["comunidad"] == comunidades[0]]["salario_medio"].values[0]
                legend_elements = [mpatches.Patch(facecolor=comunidad_color_dict[comunidades[0]], edgecolor='none', label=comunidades[0])]
                if len(eleccion_comunidad) > 1:
                    comunidades[1] = eleccion_comunidad[1]
                    valores[1] = df_salario_medio[df_salario_medio["comunidad"] == comunidades[1]]["salario_medio"].values[0]
                    legend_elements = [
                        mpatches.Patch(facecolor=comunidad_color_dict[comunidad], edgecolor='none', label=comunidad) for
                        comunidad in comunidades]


                mascara = df_salario_comunidad["comunidad"].isin(comunidades)
                grafico_comunidades, ax = plt.subplots(figsize=(12, 6), facecolor='#111111')
                sns.kdeplot(data=df_salario_comunidad[mascara],
                            x="salario_medio",
                            hue='comunidad',
                            fill=True,
                            common_norm=False,
                            palette=comunidad_color_dict,
                            cut= 0,
                            ax=ax)

                ax.set_xlabel('Salario Medio', color='orange', fontsize= 15)
                plt.xticks([i for i in range(min_salario, max_salario, 5000)], rotation=45)
                ax.set_ylabel('Densidad', color='orange', fontsize= 15)


                plt.legend(handles=legend_elements, loc='upper right', frameon=False, fontsize=12, labelcolor='#FFFFFF')
                #plt.legend('comunidad', loc='best', fontsize=10, labelcolor="#FFFFFF", facecolor='#111111')


                grafico_comunidades.set_facecolor('#111111')
                ax.set_facecolor('#111111')
                ax.spines['bottom'].set_color('#FFFFFF')
                ax.spines['top'].set_color('#FFFFFF')
                ax.spines['right'].set_color('#FFFFFF')
                ax.spines['left'].set_color('#FFFFFF')
                ax.tick_params(axis='x', colors='#FFFFFF')
                ax.tick_params(axis='y', colors='#111111')
                st.pyplot(grafico_comunidades, use_container_width=True)


        with columna_indicador:

            trace1 = go.Indicator(mode="gauge+number",
                                  gauge={'axis': {'range': [0, 50000]}},
                                  value=valores[0],
                                  title={'text': f"Salario Medio {comunidades[0]}", "font":{"color":"orange"}})

            trace2 = go.Indicator(mode="gauge+number",
                                  gauge={'axis': {'range': [0, 50000]}},
                                  value=valores[1],
                                  title={'text': f"Salario Medio {comunidades[1]}", "font":{"color":"orange"}})

            comparacion_comunidades = make_subplots(rows=2,
                                                    cols=1,
                                                    specs=[[{'type': 'indicator'}], [{'type': 'indicator'}]],
                                                    vertical_spacing=0.2)

            comparacion_comunidades.append_trace(trace1, row=1, col=1)
            comparacion_comunidades.append_trace(trace2, row=2, col=1)
            comparacion_comunidades.update_layout(paper_bgcolor='rgb(17,17,17)',
                                                  plot_bgcolor='rgb(17,17,17)',
                                                  margin=dict(l=0, r=0, t=50, b=10),
                                                  width=480, height=440)

            st.plotly_chart(comparacion_comunidades, use_container_width=True)


    ###################################################### APARTADO RANK ######################################################
    with tab3:

        columna_texto_3, columna_salario_rango = st.columns((1, 2))

        with columna_texto_3:
            st.header(":orange[_Salario_]", divider="orange", help="Gráfico interactivo")
            st.markdown(
                '<p class="big-font">Antes de atender al gráfico de la derecha se hace necesario definir cada uno de los rangos. En primer lugar definimos el perfíl Junior como aquel que cuenta entre 0 y 1 año de experiencia. A este le sigue el perfíl Mid, contando entre 2 y 4 años. Por último se encuentran los rangos con mayor maestría, siendo el Senior el que presenta entre 5 y 7 años y el Lead con más de 8.<br>Teniendo esto en cuenta, observamos como los perfiles junior, como cabe esperar, tienen el menor rango salarial, estando la media en 24.000€ brutos anuales. A medida que aumenta la experiencia notamos como el salario aumenta de forma acorde, llegando a alcanzar para los perfiles Lead una media salarial bruta de 54.000€ anuales.</p>',
                unsafe_allow_html=True)

        with columna_salario_rango:

            ############## GRAFICO SALARIO-RANGO #####################
            ##########################################################
            df["rango"] = df["experiencia"].apply(intervalo_experiencia)
            df_rango_salario = df.groupby(by="rango")[["salario_min", "salario_max"]].mean().reset_index()
            df_rango_salario["salario_medio"] = (df_rango_salario["salario_min"] + df_rango_salario["salario_max"]) / 2
            for col in df_rango_salario.columns[1:]:
                df_rango_salario[col] = df_rango_salario[col].apply(lambda x: int(x))

            rango_salario = go.Figure(
                go.Bar(x=df_rango_salario["rango"], y=df_rango_salario["salario_min"], name='Salario Mínimo', marker=dict(color="#66B78D")))
            rango_salario.add_trace(
                go.Bar(x=df_rango_salario["rango"], y=df_rango_salario["salario_medio"], name='Salario Medio', marker=dict(color="#B3BA68")))
            rango_salario.add_trace(
                go.Bar(x=df_rango_salario["rango"], y=df_rango_salario["salario_max"], name='Salario Máximo', marker=dict(color="#FFBD45")))
            rango_salario.update_layout(barmode='group',
                                        xaxis={'categoryorder': 'total ascending'},
                                        font=dict(family="Courier New, monospace", size=20, color="#000000"),
                                        legend=dict(x=0, y=1, font=dict(size=20)),
                                        width=770,
                                        height=470,
                                        margin=dict(l=200, r=0, t=80, b=0),
                                        paper_bgcolor='rgb(17,17,17)',
                                        plot_bgcolor='rgb(17,17,17)')

            st.plotly_chart(rango_salario, use_container_width=True)

        ############################################################################################################
        st.divider()
        ############################################################################################################

        columna_modalidad_rango, columna_texto_4  = st.columns((3, 2))

        with columna_texto_4:
            st.header(":orange[_Modalidad_]", divider="orange", help="Gráfico interactivo")
            st.markdown(
                '<p class="big-font">El hallazgo más significativo se observa en los perfiles Junior, donde se encuentra que el 23% de los empleos requieren presencialidad en oficina. No es de extrañar si pensamos que son perfiles sin o con poca experiencia, lo que requiere de una mayor supervisión para su desarrollo, siendo esta tarea más sencilla en oficina.<br>'
                'Por otro lado, apreciamos como la modalidad remota cobra mayor significación a medida que el rango y por tanto la responsabilidad aumentan, siendo los puestos presenciales poco requeridos (entorno al 9%).<br>'
                'Finalmente se tiene que la modalidad híbrida en los primeros años de experiencia se mantiene sobre el 35% de los empleos, descendiendo gradualmente hasta el 18% en los perfiles Lead.</p>',
                unsafe_allow_html=True)

        with columna_modalidad_rango:

            ############## GRAFICO PRESENCIALIDAD-RANGO ##############
            ##########################################################
            df_rango_presencialidad = df[df["presencialidad"] != "no especificado"].groupby(by="rango")["presencialidad"].value_counts(normalize=True).reset_index()
            df_rango_presencialidad = df_rango_presencialidad.pivot_table(index="rango", columns="presencialidad",values="proportion").reset_index()
            for col in df_rango_presencialidad.columns[1:]:
                df_rango_presencialidad[col] = round(df_rango_presencialidad[col] * 100)
            df_rango_presencialidad = df_rango_presencialidad.sort_values(by="remoto")

            presencialidad_rango = go.Figure(
                data=[go.Bar(x=df_rango_presencialidad.rango, y=df_rango_presencialidad.presencial, name="Presencial", text=df_rango_presencialidad.presencial, marker_color="#C4E6C3"),
                      go.Bar(x=df_rango_presencialidad.rango, y=df_rango_presencialidad.hibrido, name="Hibrido", text=df_rango_presencialidad.hibrido, marker_color="#66B78D"),
                      go.Bar(x=df_rango_presencialidad.rango, y=df_rango_presencialidad.remoto, name="Remoto", text=df_rango_presencialidad.remoto, marker_color="#2A7271")])

            presencialidad_rango.update_layout(xaxis_type='category',
                                               yaxis_title="Porcentaje",
                                               paper_bgcolor='rgb(17,17,17)',
                                               plot_bgcolor='rgb(17,17,17)',
                                               legend=dict(x=0, y=1, font=dict(size=20)),
                                               font=dict(family="Courier New, monospace", size=20, color="#000000"),
                                               width=760,
                                               height=490,
                                               margin=dict(l=0, r=50, t=85, b=0),
                                               autosize=True)



            st.plotly_chart(presencialidad_rango, use_container_width=True)

            #width = st.sidebar.slider("plot width", 100, 1000, 10)
            #height = st.sidebar.slider("plot height", 100, 1000, 10)

