from database.DatabaseConnection import DatabaseConnection
import psycopg2

def create_artigo(codigo, nome, publicacao, data, autor, caminho_pdf=None):
    db = DatabaseConnection()
    conn = db.connect()
    try:
        cur = conn.cursor()
        if caminho_pdf:
            with open(caminho_pdf, 'rb') as f:
                pdf_bytes = f.read()
            cur.execute("""
                INSERT INTO artigopublicado (codigo, nome, publicacao, data, autor, arquivo_pdf)
                VALUES (%s, %s, %s, %s, %s, %s)
            """, (codigo, nome, publicacao, data, autor, psycopg2.Binary(pdf_bytes)))
        else:
            cur.execute("""
                INSERT INTO artigopublicado (codigo, nome, publicacao, data, autor)
                VALUES (%s, %s, %s, %s, %s)
            """, (codigo, nome, publicacao, data, autor))
        conn.commit()
        print(" Artigo inserido com sucesso.")
    except Exception as e:
        print("Erro ao criar artigo:", e)
    finally:
        db.disconnect()

def get_artigos():
    db = DatabaseConnection()
    conn = db.connect()
    try:
        cur = conn.cursor()
        cur.execute("SELECT codigo, nome, publicacao, data, autor FROM artigopublicado")
        return cur.fetchall()
    except Exception as e:
        print("Erro ao buscar artigos:", e)
        return []
    finally:
        db.disconnect()

def update_artigo(codigo, nome, publicacao, data, autor):
    db = DatabaseConnection()
    conn = db.connect()
    try:
        cur = conn.cursor()
        cur.execute("""
            UPDATE artigopublicado
            SET nome = %s, publicacao = %s, data = %s, autor = %s
            WHERE codigo = %s
        """, (nome, publicacao, data, autor, codigo))
        conn.commit()
        print(" Artigo atualizado com sucesso.")
    except Exception as e:
        print("Erro ao atualizar artigo:", e)
    finally:
        db.disconnect()

def delete_artigo(codigo):
    db = DatabaseConnection()
    conn = db.connect()
    try:
        cur = conn.cursor()
        cur.execute("DELETE FROM artigopublicado WHERE codigo = %s", (codigo,))
        conn.commit()
        print(" Artigo deletado com sucesso.")
    except Exception as e:
        print("Erro ao deletar artigo:", e)
    finally:
        db.disconnect()

def download_pdf_artigo(codigo, caminho_saida):
    db = DatabaseConnection()
    conn = db.connect()
    try:
        cur = conn.cursor()
        cur.execute("SELECT arquivo_pdf FROM artigopublicado WHERE codigo = %s", (codigo,))
        pdf_bytes = cur.fetchone()[0]
        if pdf_bytes:
            with open(caminho_saida, 'wb') as f:
                f.write(pdf_bytes)
            print(f" PDF do artigo salvo em {caminho_saida}")
        else:
            print(" Nenhum PDF encontrado para este artigo.")
    except Exception as e:
        print("Erro ao baixar PDF do artigo:", e)
    finally:
        db.disconnect()

def upload_pdf_artigo(codigo, caminho_pdf):
    db = DatabaseConnection()
    conn = db.connect()
    try:
        with open(caminho_pdf, 'rb') as f:
            pdf_bytes = f.read()
        cur = conn.cursor()
        cur.execute("""
            UPDATE artigopublicado
            SET arquivo_pdf = %s
            WHERE codigo = %s
        """, (psycopg2.Binary(pdf_bytes), codigo))
        conn.commit()
        print(f"✅ PDF inserido no artigo com codigo {codigo}.")
    except Exception as e:
        print("Erro ao inserir PDF no artigo:", e)
    finally:
        db.disconnect()

