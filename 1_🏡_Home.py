import streamlit as st
import pandas as pd

# Configurando a pagina

st.set_page_config(
    layout='centered'

)

st.markdown("# FIFA 2023 ⚽ - OFICIAL!")
st.sidebar.markdown("Desenvovimento: Amanda Beuthner")


st.link_button(
    label="Acesse a base de dados no Kaggle",
    url="https://www.kaggle.com/datasets",
    type="primary"
)

df = pd.read_csv("datasets/CLEAN_FIFA23_official_data.csv")
df

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
