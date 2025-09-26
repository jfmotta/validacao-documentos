import streamlit as st

st.set_page_config(page_title="Validação de Documentos", page_icon="📄")

st.title("📄 Validador de Documentos")
st.write("Digite os dados abaixo para validar futuramente:")

cpf = st.text_input("CPF", placeholder="Ex: 529.982.247-25")
rg = st.text_input("RG", placeholder="Ex: 12.345.678-9")

if st.button("Validar"):
    st.info("Validação será implementada em breve.")

