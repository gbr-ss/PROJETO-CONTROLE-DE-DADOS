from fastapi import FastAPI
import funcao
app = FastAPI(title="Gerenciador de Produtos") 

@app.get("/")
def home():
    return {"mensagem": "Bem-Vindo ao Gerenciador de Produtos e Estoque"}

@app.post("/produtos")
def criar_produto(nome: str, categoria: str, preco: int, quantidade: float):
    funcao.inserir_produtos(nome, categoria, preco ,quantidade)
    return{"mensagem": "Produto adicionado com sucesso"}