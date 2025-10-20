from fastapi import FastAPI
import funcao
app = FastAPI(title="Gerenciador de Filmes") 

@app.get("/")
def home():
    return {"mensagem": "Bem-Vindo ao Gerenciador de Produtos e Estoque"}