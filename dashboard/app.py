import streamlit as st
import pandas as pd
import psycopg2
import os

st.set_page_config(page_title="Ranking Powers", layout="wide")

# Conexão com banco de dados
conn = psycopg2.connect(
    host=os.getenv("DB_HOST"),
    port=os.getenv("DB_PORT"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    dbname=os.getenv("DB_NAME")
)

# Consulta de ranking
df = pd.read_sql("SELECT recipient_name, COUNT(*) as total FROM powers GROUP BY recipient_name ORDER BY total DESC", conn)

st.title("🏆 Ranking de Powers Recebidos")
st.dataframe(df, use_container_width=True)
