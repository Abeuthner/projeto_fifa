import streamlit as st
import pandas as pd

# Configurando a pagina

st.set_page_config(
    page_title="Jogadores",
    layout="wide",
    page_icon='🏃'
    
)

df = st.session_state["data"]