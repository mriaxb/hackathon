import streamlit as st
import pandas as pd
from st_aggrid import AgGrid


with st.form(key="include_cliente"):
    input_name = st.text_input(label="Insira seu nome")
    input_age = st.number_input(label="Insira sua idade", format = "%d", step = 1)
    input_occupation = st.selectbox("Selecione sua profissão", ["Desenvolvedor", "musico"]);
    input_button_submit = st.form_submit_button(label="Concluir")



st.write("Clientes");
df = pd.read_csv('https://raw.githubusercontent.com/fivethirtyeight/data/master/airline-safety/airline-safety.csv')
AgGrid(df)