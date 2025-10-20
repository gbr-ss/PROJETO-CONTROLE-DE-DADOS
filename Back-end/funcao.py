from conexao import conectar

def criar_tabela():
    conexao, cursor = conectar()
    if conexao:
        try:
            cursor.execute("""
            CREATE TABLE  IF NOT EXISTS produtos (
            id SERIAL PRIMARY KEY,
            nome VARCHAR(100) NOT NULL,
            categoria VARCHAR(50),
            preco NUMERIC(10,2),
            quantidade INT
            );
            """)
            conexao.commit()
        except Exception as erro:
            print(f"Erro ao criar a tabela {erro}")
        finally:
            cursor.close()
            conexao.close()
criar_tabela()

def inserir_produtos(nome, categoria, preco ,quantidade):
    conexao, cursor = conectar()
    if conexao:
        try:
            cursor.execute(
                "INSERT INTO produtos (nome, categoria, preco ,quantidade) VALUES (%s, %s, %s, %s)",
                (nome, categoria, preco ,quantidade)
            )
            conexao.commit()
        except Exception as erro:
            print(f"Erro ao inserir filmes {erro}")
        finally:
            cursor.close()
            conexao.close()

def exibir_produtos():
    conexao, cursor = conectar()
    if conexao:
        try:
            cursor.execute(
                "SELECT * FROM produtos ORDER BY id"
            )
            return cursor.fetchall()
        except Exception as erro:
            print(f"Erro ao mostrar os produtos")
        finally:
            cursor.close()
            conexao.close()

def atualizar_produtos(id_produtos, nova_quantidade):
    conexao, cursor = conectar()
    if conexao:
        try:
            cursor.execute(
                "UPDATE produtos SET quantidade = %s WHERE id = %s",
                (id_produtos, nova_quantidade)
            )
            conexao.commit()
        except Exception as erro:
            print(f"Erro ao tentar atuaizar o produtos {erro}")
        finally:
            cursor.close()
            conexao.close()

def atualizar_preco(id_produtos, nova_preco):
    conexao, cursor = conectar()
    if conexao:
        try:
            cursor.execute(
                "UPDATE produtos SET preco = %s WHERE id = %s",
                (id_produtos, nova_preco)
            )
            conexao.commit()
        except Exception as erro:
            print(f"Erro ao tentar atuaizar o produtos {erro}")
        finally:
            cursor.close()
            conexao.close()

def deletar_filmes(id_produtos):
    conexao, cursor = conectar()
    if conexao:
        try:
            cursor.execute("DELETE FROM produtos WHERE id = ?", (id_produtos,))
            conexao.commit()
        except Exception as erro:
            print(f"Erro ao deletar o produtos ")
        finally:
            cursor.close()
            conexao.close()

def buscar_filmes(id_produtos):    
    conexao, cursor = conectar()
    if conexao:
        try:
            cursor.execute(
                "SELECT * FROM produtos WHERE  id = %s", (id_produtos,)
            )
            return cursor.fetchone()
        except Exception as erro:
            print(f"Erro ao mostrar  o produtos")
        finally:
            cursor.close()
            conexao.close()