import streamlit as st
import requests
#URL da API FastAPI
API_URL = "http://127.0.0.1:8000"

#Roda o streamlit
# python -m streamlit run app.py
st.set_page_config(page_title="Gerenciador de Produtos",page_icon="📦")
st.title("📦Gerenciador de produtos")

#Menu lateral
menu = st.sidebar.radio("Navegação", ["Catalogo", "Adicionar produtos","Atualizar produtos"])
if menu == "Catalogo":
    st.subheader("Todos os produtos disponiveis")
    response = requests.get(f"{API_URL}/produtos")
    if response.status_code == 200:
        produtos = response.json().get("produtos",[])
        if produtos:
            st.dataframe(produtos)
    else:
        st.error("Erro ao acessar a API")

        
elif menu == "Adicionar produtos":
    st.subheader("➕ adicionar produtos")
    nome = st.text_input("Nome do produtos")
    categoria = st.text_input("Categoria do produtos")
    preco = st.number_input("Preço de Lançamento", min_value=0, step=1)
    quantidade=st.number_input("Quantidade ", min_value=0,step=1)
    if st.button("Salvar produtos"):
        dados = {"nome": nome,"categoria": categoria,"preco": preco,"quantidade":quantidade}
        response = requests.post(f"{API_URL}/produtos",params=dados)
        if response.status_code == 200:
            st.success("produtos adicionando com sucesso!")
        else:
            st.error("Erro ao adicionar o produtos")
            
elif menu == "Atualizar produtos":
    st.subheader("✏️ Atualizar produtos")
    id_produto = st.number_input("ID do produto", min_value=1, step=1)
    novo_preco = st.number_input("Novo preço", min_value=0.0, step=0.1)
    nova_quantidade = st.number_input("Nova quantidade ", min_value=0, step=1)
    if st.button("Atualizar o produto"):
        url_preco = f"http://127.0.0.1:8000/produtos/{id_produto}"
