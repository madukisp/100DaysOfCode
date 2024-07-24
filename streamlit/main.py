import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Home",
    page_icon="🏠",
    layout="centered",
    initial_sidebar_state="collapsed"
)

st.sidebar.success("Select a page above.")

with st.container():
    st.write("# Welcome to Streamlit!")
    st.write("Select a page from the sidebar to get started. [link](https://docs.streamlit.io/get-started)")

@st.cache_data
def carregar_dados():
    tabela = pd.read_csv("resultados.csv")
    return tabela

with st.container():
    st.write("---")
    qtdade_dias = st.selectbox("Quantidade de dias", ["7D", "15D", "30D"])
    num_dias = int(qtdade_dias.replace("D", ""))
    dados = carregar_dados()
    dados = dados[-num_dias:]
    st.area_chart(dados, x="Data", y="Contratos")