from db_connection.DatabaseConnection import DatabaseConnection

def get_frentes():
    db = DatabaseConnection()
    conn = db.connect()
    try:
        cur = conn.cursor()
        cur.execute("SELECT codigo, nome, tipo, descricao, datacriacao FROM frentesdetrabalho")
        rows = cur.fetchall()
        return [
            {
                'codigo': r[0],
                'nome': r[1],
                'tipo': r[2],
                'descricao': r[3],
                'datacriacao': str(r[4])
            } for r in rows
        ]
    finally:
        db.disconnect()


def get_frente_por_codigo(codigo):
    db = DatabaseConnection()
    conn = db.connect()
    try:
        cur = conn.cursor()
        cur.execute("SELECT codigo, nome, tipo, descricao, datacriacao FROM frentesdetrabalho WHERE codigo = %s", (codigo,))
        r = cur.fetchone()
        if r:
            return {
                'codigo': r[0],
                'nome': r[1],
                'tipo': r[2],
                'descricao': r[3],
                'datacriacao': str(r[4])
            }
        return None
    finally:
        db.disconnect()


def create_frente(codigo, nome, tipo, descricao, datacriacao):
    db = DatabaseConnection()
    conn = db.connect()
    try:
        cur = conn.cursor()
        cur.execute("""
            INSERT INTO frentesdetrabalho (codigo, nome, tipo, descricao, datacriacao)
            VALUES (%s, %s, %s, %s, %s)
        """, (codigo, nome, tipo, descricao, datacriacao))
        conn.commit()
    finally:
        db.disconnect()


def update_frente(codigo, data):
    db = DatabaseConnection()
    conn = db.connect()
    try:
        cur = conn.cursor()
        cur.execute("""
            UPDATE frentesdetrabalho
            SET nome = %s, tipo = %s, descricao = %s, datacriacao = %s
            WHERE codigo = %s
        """, (
            data['nome'], data['tipo'], data['descricao'],
            data['datacriacao'], codigo
        ))
        conn.commit()
    finally:
        db.disconnect()


def delete_frente(codigo):
    db = DatabaseConnection()
    conn = db.connect()
    try:
        cur = conn.cursor()
        cur.execute("DELETE FROM frentesdetrabalho WHERE codigo = %s", (codigo,))
        conn.commit()
        cur.close()  
    finally:
        conn.close()
