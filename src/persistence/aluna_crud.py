from db_connection.DatabaseConnection import DatabaseConnection

def get_alunas():
    db = DatabaseConnection()
    conn = db.connect()
    try:
        cur = conn.cursor()
        cur.execute("SELECT * FROM Aluna")
        rows = cur.fetchall()
        return [
            {
                'matricula': r[0],
                'bolsa': r[1],
                'nomecurso': r[2],
                'instituicaocurso': r[3],
                'departamento': r[4],
                'instituicao': r[5]
            } for r in rows
        ]
    finally:
        db.disconnect()

def get_aluna_por_matricula(matricula):
    db = DatabaseConnection()
    conn = db.connect()
    try:
        cur = conn.cursor()
        cur.execute("SELECT * FROM Aluna WHERE matricula = %s", (matricula,))
        r = cur.fetchone()
        if r:
            return {
                'matricula': r[0],
                'bolsa': r[1],
                'nomecurso': r[2],
                'instituicaocurso': r[3],
                'departamento': r[4],
                'instituicao': r[5]
            }
        return None
    finally:
        db.disconnect()

def create_aluna(matricula, bolsa, nomecurso, instituicaocurso, departamento, instituicao):
    db = DatabaseConnection()
    conn = db.connect()
    try:
        cur = conn.cursor()
        cur.execute("""
            INSERT INTO Aluna (matricula, bolsa, nomecurso, instituicaocurso, departamento, instituicao)
            VALUES (%s, %s, %s, %s, %s, %s)
        """, (matricula, bolsa, nomecurso, instituicaocurso, departamento, instituicao))
        conn.commit()
    finally:
        db.disconnect()

def update_aluna(matricula, data):
    db = DatabaseConnection()
    conn = db.connect()
    try:
        cur = conn.cursor()
        cur.execute("""
            UPDATE Aluna
            SET bolsa = %s, nomecurso = %s, instituicaocurso = %s,
                departamento = %s, instituicao = %s
            WHERE matricula = %s
        """, (
            data['bolsa'], data['nomecurso'], data['instituicaocurso'],
            data['departamento'], data['instituicao'], matricula
        ))
        conn.commit()
    finally:
        db.disconnect()

def delete_aluna(matricula):
    db = DatabaseConnection()
    conn = db.connect()
    try:
        cur = conn.cursor()
        cur.execute("DELETE FROM Aluna WHERE matricula = %s", (matricula,))
        conn.commit()
    finally:
        db.disconnect()
