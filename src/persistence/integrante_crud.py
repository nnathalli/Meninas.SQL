from db_connection.DatabaseConnection import DatabaseConnection

def get_integrantes():
    db = DatabaseConnection()
    conn = db.connect()
    try:
        cur = conn.cursor()
        cur.execute("SELECT matricula, nome, datanasc, dataentrada, email, telefone FROM integrante")

        rows = cur.fetchall()
        return [
            {
                'matricula': r[0],
                'nome': r[1],
                'datanasc': r[2],
                'dataentrada': r[3],
                'email': r[4],
                'telefone': r[5]
            } for r in rows
        ]
    finally:
        db.disconnect()



def get_integrante_por_matricula(matricula):
    db = DatabaseConnection()
    conn = db.connect()
    try:
        cur = conn.cursor()
        cur.execute("SELECT matricula, nome, datanasc, dataentrada, email, telefone FROM integrante WHERE matricula = %s", (matricula,))
        r = cur.fetchone()
        if r:
            return {
                'matricula': r[0],
                'nome': r[1],
                'email': r[4],
                'telefone': r[5]
            }
        return None
    finally:
        db.disconnect()


def create_integrante(matricula, nome, datanasc, dataentrada, email, telefone):
    db = DatabaseConnection()
    conn = db.connect()
    try:
        cur = conn.cursor()
        cur.execute("""
            INSERT INTO integrante (matricula, nome, datanasc, dataentrada, email, telefone)
            VALUES (%s, %s, %s, %s, %s, %s)
        """, (matricula, nome, datanasc, dataentrada, email, telefone))
        conn.commit()
    finally:
        db.disconnect()


def update_integrante(matricula, data):
    db = DatabaseConnection()
    conn = db.connect()
    try:
        cur = conn.cursor()
        cur.execute("""
            UPDATE integrante
            SET nome = %s, datanasc = %s, dataentrada = %s, email = %s, telefone = %s
            WHERE matricula = %s
        """, (
            data['nome'], data['datanasc'], data['dataentrada'],
            data['email'], data['telefone'], matricula
        ))
        conn.commit()
    finally:
        db.disconnect()


def delete_integrante(matricula):
    db = DatabaseConnection()
    conn = db.connect()
    try:
        cur = conn.cursor()
        cur.execute("DELETE FROM integrante WHERE matricula = %s", (matricula,))
        conn.commit()
    finally:
        db.disconnect()
