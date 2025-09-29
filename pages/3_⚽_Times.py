import streamlit as st
import pandas as pd

# Configurando a pagina

st.set_page_config(
    page_title="Jogadores",
    layout="wide",
    page_icon='🏃'
    
)

df = st.session_state["data"]

clubes = sorted(df["Club"].dropna().unique())
club = st.sidebar.selectbox("Clube", clubes)

df_filtered = df[df['Club'] == club].set_index('Name').sort_index()

st.header(df_filtered["Club"][0])
st.markdown(f'[Bandeira do Club]({df_filtered["Club Logo"][0]})')

filtro_colunas = ["Age", "Photo", "Flag", "Overall", "Value(£)", "Wage(£)", "Joined",
                  "Height(cm.)", "Weight(lbs.)",
                  "Contract Valid Until", "Release Clause(£)"]

st.dataframe(df_filtered[filtro_colunas],
             column_config= {
                 "Overall": st.column_config.ProgressColumn("Overall", format="%d", min_value=0, max_value=100),
                 "Wage(£)": st.column_config.ProgressColumn("Weekly Wage", format="£ %f", min_value=0, max_value=df_filtered["Wage(£)"].max()),
                 "Photo": st.column_config.LinkColumn(),
                 "Wage(£)": st.column_config.ProgressColumn("Weekly Wage", format="£ %f", min_value=0, max_value=df_filtered["Wage(£)"].max()),
                 "Flag": st.column_config.LinkColumn("Country"),
                 "Value(£)": st.column_config.NumberColumn("Value(£)", format= 'localized'),
                 "Release Clause(£)": st.column_config.NumberColumn("Release Clause(£)", format= 'localized')
                 }) 


