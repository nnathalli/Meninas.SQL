from database.DatabaseConnection import DatabaseConnection
import psycopg2

def create_livro(codigo, nome, descricao, editora, estoque, caminho_pdf=None):
    db = DatabaseConnection()
    conn = db.connect()
    try:
        cur = conn.cursor()
        if caminho_pdf:
            with open(caminho_pdf, 'rb') as f:
                pdf_bytes = f.read()
            cur.execute("""
                INSERT INTO livros (codigo, nome, descricao, editora, estoque, arquivo_pdf)
                VALUES (%s, %s, %s, %s, %s, %s)
            """, (codigo, nome, descricao, editora, estoque, psycopg2.Binary(pdf_bytes)))
        else:
            cur.execute("""
                INSERT INTO livros (codigo, nome, descricao, editora, estoque)
                VALUES (%s, %s, %s, %s, %s)
            """, (codigo, nome, descricao, editora, estoque))
        conn.commit()
        print(" Livro inserido com sucesso.")
    except Exception as e:
        print("Erro ao criar livro:", e)
    finally:
        db.disconnect()

def get_livros():
    db = DatabaseConnection()
    conn = db.connect()
    try:
        cur = conn.cursor()
        cur.execute("SELECT codigo, nome, descricao, editora, estoque FROM livros")
        return cur.fetchall()
    except Exception as e:
        print("Erro ao buscar livros:", e)
        return []
    finally:
        db.disconnect()

def update_livro(codigo, nome, descricao, editora, estoque):
    db = DatabaseConnection()
    conn = db.connect()
    try:
        cur = conn.cursor()
        cur.execute("""
            UPDATE livros
            SET nome = %s, descricao = %s, editora = %s, estoque = %s
            WHERE codigo = %s
        """, (nome, descricao, editora, estoque, codigo))
        conn.commit()
        print(" Livro atualizado com sucesso.")
    except Exception as e:
        print("Erro ao atualizar livro:", e)
    finally:
        db.disconnect()

def delete_livro(codigo):
    db = DatabaseConnection()
    conn = db.connect()
    try:
        cur = conn.cursor()
        cur.execute("DELETE FROM livros WHERE codigo = %s", (codigo,))
        conn.commit()
        print(" Livro deletado com sucesso.")
    except Exception as e:
        print("Erro ao deletar livro:", e)
    finally:
        db.disconnect()

def download_pdf_livro(codigo, caminho_saida):
    db = DatabaseConnection()
    conn = db.connect()
    try:
        cur = conn.cursor()
        cur.execute("SELECT arquivo_pdf FROM livros WHERE codigo = %s", (codigo,))
        pdf_bytes = cur.fetchone()[0]
        if pdf_bytes:
            with open(caminho_saida, 'wb') as f:
                f.write(pdf_bytes)
            print(f" PDF do livro salvo em {caminho_saida}")
        else:
            print(" Nenhum PDF encontrado para este livro.")
    except Exception as e:
        print("Erro ao baixar PDF do livro:", e)
    finally:
        db.disconnect()

def upload_pdf_livro(codigo, caminho_pdf):
    db = DatabaseConnection()
    conn = db.connect()
    try:
        with open(caminho_pdf, 'rb') as f:
            pdf_bytes = f.read()
        cur = conn.cursor()
        cur.execute("""
            UPDATE livros
            SET arquivo_pdf = %s
            WHERE codigo = %s
        """, (psycopg2.Binary(pdf_bytes), codigo))
        conn.commit()
        print(f"✅ PDF inserido no livro com codigo {codigo}.")
    except Exception as e:
        print("Erro ao inserir PDF no livro:", e)
    finally:
        db.disconnect()
