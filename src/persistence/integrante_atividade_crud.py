from db_connection.DatabaseConnection import DatabaseConnection

def associar_integrante_atividade(matricula, codigo_atividade):
    db = DatabaseConnection()
    conn = db.connect()
    try:
        cur = conn.cursor()
        cur.execute("""
            INSERT INTO integranteatividade (matricula, codigoatividade)
            VALUES (%s, %s)
            ON CONFLICT DO NOTHING
        """, (matricula, codigo_atividade))
        conn.commit()
    finally:
        db.disconnect()

def desassociar_integrante_atividade(matricula, codigo_atividade):
    db = DatabaseConnection()
    conn = db.connect()
    try:
        cur = conn.cursor()
        cur.execute("""
            DELETE FROM integranteatividade
            WHERE matricula = %s AND codigoatividade = %s
        """, (matricula, codigo_atividade))
        conn.commit()
    finally:
        db.disconnect()

def get_integrantes_por_atividade(codigo_atividade):
    db = DatabaseConnection()
    conn = db.connect()
    try:
        cur = conn.cursor()
        cur.execute("""
            SELECT i.matricula, i.nome
            FROM integrante i
            JOIN integranteatividade ia ON i.matricula = ia.matricula
            WHERE ia.codigoatividade = %s
        """, (codigo_atividade,))
        return [{'matricula': r[0], 'nome': r[1]} for r in cur.fetchall()]
    finally:
        db.disconnect()