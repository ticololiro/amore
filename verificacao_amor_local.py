
import streamlit as st
from datetime import datetime
from PIL import Image
import unicodedata
import os

def normalizar_texto(texto):
    return unicodedata.normalize('NFKD', texto).encode('ASCII', 'ignore').decode().strip().lower()

st.title("💖 Verificação de Amor 💖")
st.markdown("Responda com atenção... o coração não mente! 💘")

nome = st.text_input("💬 Nome completo:")
data_encontro = st.date_input("📅 Data do primeiro encontro:")
data_namoro = st.date_input("📅 Data do início do namoro:")
local_beijo = st.text_input("📍 Local do primeiro beijo:")

if st.button("💌 Validar informações"):
    nome_correto = "Davi Zellman gockino e Silva"
    data_encontro_correta = datetime(2025, 2, 28).date()
    data_namoro_correta = datetime(2025, 6, 1).date()
    local_beijo_correto = "Parque Trianon"

    if (
        normalizar_texto(nome) == normalizar_texto(nome_correto)
        and data_encontro == data_encontro_correta
        and data_namoro == data_namoro_correta
        and normalizar_texto(local_beijo) == normalizar_texto(local_beijo_correto)
    ):
        st.success("💘 Todas as informações estão corretas! Amor verdadeiro detectado! 💞")
        imagem = Image.open("imagem_amor.png")
        st.image(imagem, caption="💖 Amor verdadeiro confirmado!", use_container_width=True)
    else:
        st.error("❌ Alguma das informações está incorreta... tente novamente com carinho 💔")
        imagem = Image.open("imagem_triste.png")
        st.image(imagem, caption="💔 Ops! Algo não bateu...", use_container_width=True)
