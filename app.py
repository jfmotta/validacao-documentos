import streamlit as st

st.set_page_config(page_title="Validador de Documentos", page_icon="📄")

st.title("📄 Validador de Documentos")
st.write("Digite os dados abaixo para validar:")

cpf = st.text_input("CPF", placeholder="Ex: 529.982.247-25")
rg = st.text_input("RG", placeholder="Ex: 12.345.678-9")

if st.button("Validar"):
    st.info("Validação será implementada em breve.")

from src.validar_cpf import validar_cpf
from src.validar_rg import validar_rg

if st.button("Validar"):
    if cpf:
        st.success("✅ CPF válido!" if validar_cpf(cpf) else "❌ CPF inválido.")
    if rg:
        st.success("✅ RG válido!" if validar_rg(rg) else "❌ RG inválido.")

