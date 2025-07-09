from db_connection.DatabaseConnection import DatabaseConnection

def get_atividades():
    db = DatabaseConnection()
    conn = db.connect()
    try:
        cur = conn.cursor()
        cur.execute("""
            SELECT codigo, nome, descricao, tipo, local, datahora, duracao
            FROM atividades
        """)
        rows = cur.fetchall()
        return [
            {
                'codigo': r[0],
                'nome': r[1],
                'descricao': r[2],
                'tipo': r[3],
                'local': r[4],
                'data_hora': str(r[5]),
                'duracao': str(r[6])
            } for r in rows
        ]
    finally:
        db.disconnect()


def get_atividade_por_codigo(codigo):
    db = DatabaseConnection()
    conn = db.connect()
    try:
        cur = conn.cursor()
        cur.execute("""
            SELECT codigo, nome, descricao, tipo, local, datahora, duracao
            FROM atividades WHERE codigo = %s
        """, (codigo,))
        r = cur.fetchone()
        if r:
            return {
                'codigo': r[0],
                'nome': r[1],
                'descricao': r[2],
                'tipo': r[3],
                'local': r[4],
                'data_hora': str(r[5]),
                'duracao': str(r[6])
            }
        return None
    finally:
        db.disconnect()


def create_atividade(codigo, nome, descricao, tipo, local, data_hora, duracao):
    db = DatabaseConnection()
    conn = db.connect()
    try:
        cur = conn.cursor()
        cur.execute("""
            INSERT INTO atividades (codigo, nome, descricao, tipo, local, datahora, duracao)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """, (codigo, nome, descricao, tipo, local, data_hora, duracao))
        conn.commit()
    finally:
        db.disconnect()


def update_atividade(codigo, data):
    db = DatabaseConnection()
    conn = db.connect()
    try:
        cur = conn.cursor()
        cur.execute("""
            UPDATE atividades
            SET nome = %s, descricao = %s, tipo = %s, local = %s, datahora = %s, duracao = %s
            WHERE codigo = %s
        """, (
            data['nome'], data['descricao'], data['tipo'], data['local'],
            data['data_hora'], data['duracao'], codigo
        ))
        conn.commit()
    finally:
        db.disconnect()


def delete_atividade(codigo):
    db = DatabaseConnection()
    conn = db.connect()
    try:
        cur = conn.cursor()
        cur.execute("DELETE FROM atividades WHERE codigo = %s", (codigo,))
        conn.commit()
    finally:
        db.disconnect()
