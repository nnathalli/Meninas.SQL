from database.DatabaseConnection import DatabaseConnection

def create_frente(codigo, nome, tipo, descricao, data_criacao):
    db = DatabaseConnection()
    conn = db.connect()
    try:
        cur = conn.cursor()
        cur.execute("""
            INSERT INTO frentesdetrabalho (codigo, nome, tipo, descricao, datacriacao)
            VALUES (%s, %s, %s, %s, %s)
        """, (codigo, nome, tipo, descricao, data_criacao))
        conn.commit()
    except Exception as e:
        print("Erro ao criar frente:", e)
    finally:
        db.disconnect()

def get_frentes():
    db = DatabaseConnection()
    conn = db.connect()
    try:
        cur = conn.cursor()
        cur.execute("SELECT * FROM frentesdetrabalho")
        return cur.fetchall()
    except Exception as e:
        print("Erro ao buscar frentes:", e)
        return []
    finally:
        db.disconnect()

def update_frente(codigo, nome, tipo, descricao, data_criacao):
    db = DatabaseConnection()
    conn = db.connect()
    try:
        cur = conn.cursor()
        cur.execute("""
            UPDATE frentesdetrabalho
            SET nome = %s, tipo = %s, descricao = %s, datacriacao = %s
            WHERE codigo = %s
        """, (nome, tipo, descricao, data_criacao, codigo))
        conn.commit()
    except Exception as e:
        print("Erro ao atualizar frente:", e)
    finally:
        db.disconnect()

def delete_frente(codigo):
    db = DatabaseConnection()
    conn = db.connect()
    try:
        cur = conn.cursor()
        cur.execute("DELETE FROM frentesdetrabalho WHERE codigo = %s", (codigo,))
        conn.commit()
    except Exception as e:
        print("Erro ao deletar frente:", e)
    finally:
        db.disconnect()
