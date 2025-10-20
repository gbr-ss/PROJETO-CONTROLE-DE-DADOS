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

@app.get("/produtos")
def listar_produtos():
    produtos = funcao.exibir_produtos()
    lista = []
    for linha in produtos:
        lista.append({
            "id": linha[0],           
            "nome": linha[1],
            "categoria": linha[2],
            "preco": linha[3],
            "quantidade":linha[4]
            })
    return{"produtos": lista}

@app.put("/produtos/{id_produtos}/quantidade")
def atulizar_produtos(id_produtos: int,nova_quantidade:float):
    produtos = funcao.buscar_produtos(id_produtos)
    if produtos:
        funcao.atualizar_produtos(id_produtos, nova_quantidade)
        return{"mensagem": "Produto atualizado com sucesso!"}
    else:
        return {"erro": "Produto não encontrado"}
    
@app.put("/produtos/{id_produto}/preco")
def atulizar_preco(id_produtos: int,novo_preco:float):
    produtos = funcao.buscar_produtos(id_produtos)
    if produtos:
        funcao.atualizar_preco(id_produtos, novo_preco)
        return{"mensagem": "Produto atualizado com sucesso!"}
    else:
        return {"erro": "Produto não encontrado"}
@app.delete("/estoque")
def deletar_produtos(id: int):
    funcao.deletar_produtos(id):
    return {"mensagem": "Produto Deletado com Sucesso"}