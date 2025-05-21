import streamlit as st
import openai
openai.api_key = "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"

st.set_page_config(page_title="ChatGPT Simples", page_icon="💬", layout="wide")
st.markdown("<h1 style='text-align: center;'>Chat com GPT-3.5</h1>", unsafe_allow_html=True)

prompt = st.text_input("Digite sua pergunta e pressione Enter:")

if prompt:
    st.session_state["mensagens"] = st.session_state.get("mensagens", []) + [{"role": "user", "content": prompt}]
    try:
        resposta = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=st.session_state["mensagens"]
        )
        msg = resposta.choices[0].message["content"]
        st.session_state["mensagens"].append({"role": "assistant", "content": msg})
        st.markdown(f"**Resposta:** {msg}")
    except Exception as e:
        st.error(f"Erro: {e}")
