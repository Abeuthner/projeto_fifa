import streamlit as st
import pandas as pd

df = st.session_state["data"]

clubes = sorted(df["Club"].dropna().unique())
club = st.sidebar.selectbox("Clube", clubes)

df_playes = df[(df["Club"] == club)]
players = sorted(df_playes["Name"].dropna().unique())
player = st.sidebar.selectbox("Jogadores", players)

player_stats = df[df["Name"] == player].iloc[0]


Jogador = st.markdown(f'# {player_stats["Name"]}')
st.markdown(f'[Photo do jogador]({player_stats.loc["Photo"]})')
st.markdown(f"**Clube:** {player_stats.loc['Club']}")
st.markdown(f"**Posision:** {player_stats.loc['Position']}")

col1, col2, col3 = st.columns(3)

col1.markdown(f"**Idade:** {player_stats.loc['Age']}")
col2.markdown(f"**Altura:** {player_stats.loc['Height(cm.)']/100}")
col3.markdown(f"**Peso:** {player_stats.loc['Weight(lbs.)']*0.453:.2f}")
st.divider()

st.subheader(f"Overall: {player_stats.loc['Overall']}")
st.progress(int(player_stats.loc['Overall']))


