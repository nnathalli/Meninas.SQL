from database.DatabaseConnection import DatabaseConnection

def create_atividade(codigo, nome, descricao, tipo, local, datahora, duracao):
    db = DatabaseConnection()
    conn = db.connect()
    try:
        cur = conn.cursor()
        cur.execute("""
            INSERT INTO atividades (codigo, nome, descricao, tipo, local, datahora, duracao)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """, (codigo, nome, descricao, tipo, local, datahora, duracao))
        conn.commit()
    except Exception as e:
        print("Erro ao criar atividade:", e)
    finally:
        db.disconnect()

def get_atividades():
    db = DatabaseConnection()
    conn = db.connect()
    try:
        cur = conn.cursor()
        cur.execute("SELECT * FROM atividades")
        return cur.fetchall()
    except Exception as e:
        print("Erro ao buscar atividades:", e)
        return []
    finally:
        db.disconnect()

def update_atividade(codigo, nome, descricao, tipo, local, datahora, duracao):
    db = DatabaseConnection()
    conn = db.connect()
    try:
        cur = conn.cursor()
        cur.execute("""
            UPDATE atividades
            SET nome = %s, descricao = %s, tipo = %s, local = %s, datahora = %s, duracao = %s
            WHERE codigo = %s
        """, (nome, descricao, tipo, local, datahora, duracao, codigo))
        conn.commit()
    except Exception as e:
        print("Erro ao atualizar atividade:", e)
    finally:
        db.disconnect()

def delete_atividade(codigo):
    db = DatabaseConnection()
    conn = db.connect()
    try:
        cur = conn.cursor()
        cur.execute("DELETE FROM atividades WHERE codigo = %s", (codigo,))
        conn.commit()
    except Exception as e:
        print("Erro ao deletar atividade:", e)
    finally:
        db.disconnect()
