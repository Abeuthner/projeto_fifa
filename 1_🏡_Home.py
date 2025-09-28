import streamlit as st
import pandas as pd

# Configurando a pagina

st.set_page_config(
    layout='centered'

)

df = pd.read_csv("datasets/CLEAN_FIFA23_official_data.csv")
df

st.title("FIFA 2023 ⚽!")
st.link_button(
    label="Acesse a base de dados no Kaggle",
    url="https://www.kaggle.com/datasets",
    type="primary"
)

