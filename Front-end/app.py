import streamlit as st
import requests
#URL da API FastAPI
API_URL = "http://127.0.0.1:8000"

#Roda o streamlit
# python -m streamlit run app.py
st.set_page_config(page_title="Gerenciador de Produtos",page_icon="📦")
st.title("📦Gerenciador de produtos")

#Menu lateral
menu = st.sidebar.radio("Navegação", ["Catalogo", "Adicionar produtos","Atualizar produtos","Deletar"])
if menu == "Catalogo":
    response_max_produtos = requests.get(f"http://127.0.0.1:8000/produtos/quantidade_max")
    qtd = response_max_produtos.json().get("produtos",[])

    st.subheader("Todos os produtos disponiveis")
    st.markdown(qtd[0])
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
        url_base = "http://localhost:8000/produtos"
        response_preco = requests.put(f"{url_base}/{id_produto}/preco", params={"nova_preco": novo_preco})
        response_quantidade = requests.put(f"{url_base}/{id_produto}/quantidade", params={"nova_quantidade": nova_quantidade})
        if response_preco.status_code == 200 and response_quantidade.status_code == 200:
            st.success("Produto atualizado com sucesso!")
        else:
            st.error("Erro ao atualizar o produto. Verifique o ID e tente novamente.")
elif menu == "Deletar":
    st.subheader("❌ Deletar algum objeto")
    id_produto = st.number_input("ID do produto", min_value=1, step=1)
    if st.button("Deletar"):
        url = f"http://127.0.0.1:8000/estoque?id={id_produto}"
        response = requests.delete(url)
        if response.status_code == 200:
            st.success("Produto deletado com sucesso!")
        elif response.status_code == 404:
            st.error("Produto não encontrado.")
        else:
            st.error("Erro ao deletar")