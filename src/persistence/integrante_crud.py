import psycopg2
from database.DatabaseConnection import DatabaseConnection

def create_integrante(matricula, nome, data_nasc, data_entrada, email, telefone):
    db = DatabaseConnection()
    conn = db.connect()
    try:
        cur = conn.cursor()
        cur.execute("""
            INSERT INTO integrante (matricula, nome, datanasc, dataentrada, email, telefone)
            VALUES (%s, %s, %s, %s, %s, %s)
        """, (matricula, nome, data_nasc, data_entrada, email, telefone))
        conn.commit()
    except Exception as e:
        print("Erro ao criar integrante:", e)
    finally:
        db.disconnect()

def get_integrantes():
    db = DatabaseConnection()
    conn = db.connect()
    try:
        cur = conn.cursor()
        cur.execute("SELECT * FROM integrante")
        return cur.fetchall()
    except Exception as e:
        print("Erro ao buscar integrantes:", e)
        return []
    finally:
        db.disconnect()

def update_integrante(matricula, nome, data_nasc, data_entrada, email, telefone):
    db = DatabaseConnection()
    conn = db.connect()
    try:
        cur = conn.cursor()
        cur.execute("""
            UPDATE integrante
            SET nome = %s, datanasc = %s, dataentrada = %s, email = %s, telefone = %s
            WHERE matricula = %s
        """, (nome, data_nasc, data_entrada, email, telefone, matricula))
        conn.commit()
    except Exception as e:
        print("Erro ao atualizar integrante:", e)
    finally:
        db.disconnect()

def delete_integrante(matricula):
    db = DatabaseConnection()
    conn = db.connect()
    try:
        cur = conn.cursor()
        cur.execute("DELETE FROM integrante WHERE matricula = %s", (matricula,))
        conn.commit()
    except Exception as e:
        print("Erro ao deletar integrante:", e)
    finally:
        db.disconnect()

def adicionar_foto_integrante(matricula, caminho_imagem):
    db = DatabaseConnection()
    conn = db.connect()
    try:
        with open(caminho_imagem, 'rb') as f:
            foto_binario = f.read()
        cur = conn.cursor()
        cur.execute("""
            UPDATE integrante
            SET foto = %s
            WHERE matricula = %s
        """, (psycopg2.Binary(foto_binario), matricula))
        conn.commit()
        print("Foto inserida com sucesso.")
    except Exception as e:
        print("Erro ao inserir foto:", e)
    finally:
        db.disconnect()
