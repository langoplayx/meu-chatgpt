import streamlit as st
import requests

# Chave da API Gemini 2.0 Flash
API_KEY = "AIzaSyB5gvHKwrUX1XXNxZ2CfOAI-NE1UPX3CB8"

def gerar_resposta(texto_usuario):
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={API_KEY}"
    headers = {"Content-Type": "application/json"}
    data = {
        "contents": [
            {
                "parts": [
                    {"text": texto_usuario}
                ]
            }
        ]
    }
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        resposta = response.json()
        return resposta["candidates"][0]["content"]["parts"][0]["text"]
    else:
        return f"Erro: {response.status_code} - {response.text}"

st.set_page_config(page_title="Chat Gemini", layout="wide")
st.title("Chat com Gemini 2.0 Flash")

if "historico" not in st.session_state:
    st.session_state.historico = []

pergunta = st.text_input("Digite sua pergunta", "")
if pergunta:
    st.session_state.historico.append({"pergunta": pergunta})
    resposta = gerar_resposta(pergunta)
    st.session_state.historico[-1]["resposta"] = resposta
    st.experimental_rerun()

for item in st.session_state.historico[::-1]:
    st.markdown(f"**Você:** {item['pergunta']}")
    st.markdown(f"**Gemini:** {item['resposta']}")
    st.markdown("---")
    
