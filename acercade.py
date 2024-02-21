import streamlit as st

def info():
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



    ########################################### ACERCA DE #############################################

    st.markdown("<h2 style='text-align: center; font-size: 60px;color: orange; '>Información</h2>", unsafe_allow_html=True)








if __name__ == "__info__":
    info()