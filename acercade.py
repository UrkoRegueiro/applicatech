import streamlit as st
import cv2

def info():
    st.markdown("""
                <style>
                .big-font {
                    font-size:20px;
                    color: #FFFFFF;
                }
                    
                .patata {
                    font-size:0.8px;
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
            	
            	.st-emotion-cache-1ol4dec {
            	background-color: #705202;
            	}
            	
            	

            </style>""", unsafe_allow_html=True)



    ########################################### ACERCA DE #############################################

    st.markdown("<h2 style='text-align: center; font-size: 60px;color: orange; '>Información</h2>", unsafe_allow_html=True)
    st.image("data/divider.png")
    st.markdown(
        '<p class="big-font">En esta sección, te damos la bienvenida a conocer al equipo que ha hecho posible este proyecto. Aquí encontrarás enlaces a nuestras páginas profesionales, donde puedes obtener más información sobre nosotros o ponerte en contacto.<br>Además, proporcionamos un acceso directo al repositorio del proyecto en cualquiera de los perfiles de github. Allí podrás explorar el código fuente y comprender en detalle el proceso ETL que hemos implementado, así como el EDA, la modelización y diseño de la página web, apreciando el trabajo y la dedicación que hemos invertido.<br>Esperamos que esta sección te brinde una comprensión más completa de quiénes somos y qué nos impulsa a seguir avanzando como científicos de datos. Te invitamos a explorar y descubrir más sobre nosotros y nuestros proyectos.</p>',
        unsafe_allow_html=True)

    ###################################################### INFO ######################################################
    width, height = (255, 255)
    col, columna_adrian, columna_eduardo, columna_esteban, columna_urko = st.columns((0.15,1,1,1,1))

    ################################################################
    ########## Adrián ##########

    with columna_adrian:
        st.header(":orange[&nbsp;&nbsp;&nbsp;&nbsp;_Adrián Moldes_]")
        adrian = cv2.imread(r"data/Adrian.png")
        adrian = cv2.cvtColor(adrian, cv2.COLOR_BGR2RGB)
        adrian = cv2.resize(adrian, (width, height))
        st.image(adrian)

        # Links:
        linkedin, github = st.columns((1.2,1))

        linkedin.link_button("Linkedin", "https://www.linkedin.com/in/adrianmoldes/")
        github.link_button("GitHub", "https://github.com/AdrianMoldes")

    ################################################################
    ########## Eduardo ##########

    with columna_eduardo:
        st.header(":orange[_Eduardo Velazco_]")
        eduardo = cv2.imread(r"data/Eduardo.png")
        eduardo = cv2.cvtColor(eduardo, cv2.COLOR_BGR2RGB)
        eduardo = cv2.resize(eduardo, (width, height))
        st.image(eduardo)

        # Links:
        linkedin, github = st.columns((1.2,1))

        linkedin.link_button("Linkedin", "https://www.linkedin.com/in/eduardovelazco/")
        github.link_button("GitHub", "https://github.com/e-velazco")

    ################################################################
    st.markdown(4 * '<br>', unsafe_allow_html=True)
    ########## Esteban ##########

    with columna_esteban:
        st.header(":orange[&nbsp;&nbsp;&nbsp;_Esteban Pérez_]")

        esteban = cv2.imread(r"data/Esteban.png")
        esteban = cv2.cvtColor(esteban, cv2.COLOR_BGR2RGB)
        esteban = cv2.resize(esteban, (width, height))
        st.image(esteban)

        # Links:
        linkedin, github = st.columns((1.2,1))

        linkedin.link_button("Linkedin", "https://www.linkedin.com/in/esteban-rafael-perez-lizardo/")
        github.link_button("GitHub", "https://github.com/estebanrpl")

    ################################################################
    ########## Urko ##########

    with columna_urko:
        st.header(":orange[&nbsp;&nbsp;&nbsp;_Urko Regueiro_]")

        urko = cv2.imread(r"data/Urko.png")
        urko = cv2.cvtColor(urko, cv2.COLOR_BGR2RGB)
        urko = cv2.resize(urko, (width, height))
        st.image(urko)

        # Links:
        linkedin, github = st.columns((1.2,1))

        linkedin.link_button("Linkedin", "https://www.linkedin.com/in/urkoregueiro/")
        github.link_button("GitHub", "https://github.com/UrkoRegueiro")

    st.markdown('<p class="patata">HOLA PATTATA</p>', unsafe_allow_html=True)




if __name__ == "__info__":
    info()