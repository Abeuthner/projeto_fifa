import streamlit as st
import pandas as pd
from datetime import datetime

# Configurando a pagina

st.set_page_config(
    page_title="Home",
    layout='centered',
    page_icon='🏡'
    
)

if "data" not in st.session_state:
    df = pd.read_csv("datasets/CLEAN_FIFA23_official_data.csv", index_col= 0)
    df = df[df["Contract Valid Until"] >= datetime.today().year]
    df = df[df["Value(£)"] > 0]
    df = df.sort_values(by= "Overall", ascending=False)
    st.session_state["data"] = df


st.markdown("# FIFA 2023 ⚽ - OFICIAL!")
st.sidebar.markdown("Desenvovimento: Amanda Beuthner")


st.link_button(
    label="Acesse a base de dados no Kaggle",
    url="https://www.kaggle.com/datasets",
    type="primary"
)


st.markdown(
    """
    O conjunto de dados
    de jogadores de futebol de 2017 a 2023 fornece informações 
    abrangentes sobre jogadores de futebol profissionais.
    O conjunto de dados contém uma ampla gama de atributos, incluindo dados demográficos 
    do jogador, características físicas, estatísticas de jogo, detalhes do contrato e 
    afiliações de clubes. 
    
    Com **mais de 17.000 registros**, este conjunto de dados oferece um recurso valioso para 
    analistas de futebol, pesquisadores e entusiastas interessados em explorar vários 
    aspectos do mundo do futebol, pois permite estudar atributos de jogadores, métricas de 
    desempenho, avaliação de mercado, análise de clubes, posicionamento de jogadores e 
    desenvolvimento do jogador ao longo do tempo.
"""
)
