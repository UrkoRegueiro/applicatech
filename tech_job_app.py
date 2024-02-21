################ Funciones #################

from funciones.funciones_eda import *

############################################

def tech_app():
    st.markdown("""
        <style>
        .center-font {
            font-size:20px;
            text-align: center;
            color: #FAFAFA;
        }
        </style>
        """, unsafe_allow_html=True)

    st.markdown("""
                <style>
                .big-font {
                    font-size:17px;
                    color: #FAFAFA;
                    text-align: left;

                }
                .sub-font {
                    font-size:22px;
                    color: #FAA227;
                    font-weight: bold;                    

                }
                </style>
                """, unsafe_allow_html=True)

    ################ TITULO ########################
    st.markdown("<h1 style='text-align: center;color: orange; font-size: 3em;'>Un viaje por el mercado Tech español</h1>", unsafe_allow_html=True)

    st.image("data/divider.png")
    ################ INTRO #######################
    col_1, col_2, col_3 = st.columns((0.2,1,0.2))

    col_2.markdown(
        '<p class="big-font">Esta plataforma es el resultado del trabajo en equipo llevado a cabo por Adrián Moldes, Eduardo Velazco, Esteban Pérez y Urko Regueiro como proyecto final del bootcamp de <span style="font-weight: bold; color: orange">Data Science e Inteligencia Artificial</span> de la escuela <span style="font-weight: bold; color: orange">HACK A BOSS</span>.<br>'
        'La idea de realizar un estudio pormenorizado del mercado laboral tecnólogico en España surge de nuestro propio interés en podernos incorporar a él, entendiendo al menos de forma general cuáles son las necesidades actuales y reales de las empresas que requieren este tipo de perfiles. Para conseguir nuestro objetivo, hemos llevado a cabo la tarea de extraer, transformar, cargar y analizar datos de los portales de empleo más utilizados con el objetivo de conseguir información valiosa y detallada, obteniendo una primera muestra de más de 18000 datos que seguiremos ampliando y actualizando.<br><br>'
        'En la sección <span style="font-weight: bold; color: orange">Una visión general</span> hemos querido proporcionar una panorámica completa de la situación del mercado tecnológico español. Desde la demanda de empleos por sector hasta las habilidades más demandadas. Reconocemos la importancia de comprender las tendencias generales antes de sumergirse en detalles más específicos.<br>'
        'En <span style="font-weight: bold; color: orange">Explora el mercado</span> hemos brindado la posibilidad de personalizar tu exploración, pudiendo descubrir qué stack tecnológico se adapta mejor a cada sector o entender la distribución salarial por comunidad autónoma a través de gráficos interactivos. Creemos que esta personalización permitirá obtener información precisa y relevante para saciar tu curiosidad.<br>'
        'Por último hemos diseñado un <span style="font-weight: bold; color: orange">Predictor Salarial</span> montado sobre dos modelos de Machine Learning que te permitirán, especificando ciertos parámetros, obtener un rango salarial estimado ajustado a tus características.<br><br>'
        'Queremos destacar que este proyecto no solo es una iniciativa informativa, sino también un testimonio de nuestro aprendizaje en el mundo de la ciencia de datos e inteligencia artificial. Este sitio web es el producto de un esfuerzo colaborativo de nuestro talentoso equipo, y queremos compartir contigo los frutos de nuestro trabajo. Si deseas explorar más a fondo el proceso ETL y el código detrás de esta plataforma, en la sección <span style="font-weight: bold; color: orange">Acerca de</span> encontrarás el link a nuestros perfiles de LinkedIn y GitHub, donde se reune todo el código.<br>'
        'Estamos emocionados de ofrecerte una herramienta que esperamos sea valiosa para tu comprensión del mercado laboral tecnológico en España. <br> <span style="font-weight: bold; font-size: 1.075em; color: orange">¡Sumérgete, explora y encuentra la información que te ayudará a avanzar en tu carrera en el apasionante mundo tech!</span></p>',
        unsafe_allow_html=True)

if __name__ == "__tech_app__":
    tech_app()
