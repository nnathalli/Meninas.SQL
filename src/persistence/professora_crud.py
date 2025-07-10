from db_connection.DatabaseConnection import DatabaseConnection

def get_professoras():
    db = DatabaseConnection()
    conn = db.connect()
    try:
        cur = conn.cursor()
        cur.execute("SELECT * FROM Professora")
        rows = cur.fetchall()
        return [
            {
                'matricula': r[0],
                'areaatuacao': r[1],
                'curriculo': r[2],
                'instituicao': r[3]
            } for r in rows
        ]
    finally:
        db.disconnect()

def get_professora_por_matricula(matricula):
    db = DatabaseConnection()
    conn = db.connect()
    try:
        cur = conn.cursor()
        cur.execute("SELECT * FROM Professora WHERE matricula = %s", (matricula,))
        r = cur.fetchone()
        if r:
            return {
                'matricula': r[0],
                'areaatuacao': r[1],
                'curriculo': r[2],
                'instituicao': r[3]
            }
        return None
    finally:
        db.disconnect()

def create_professora(matricula, areaatuacao, curriculo, instituicao):
    db = DatabaseConnection()
    conn = db.connect()
    try:
        cur = conn.cursor()
        cur.execute("""
            INSERT INTO Professora (matricula, areaatuacao, curriculo, instituicao)
            VALUES (%s, %s, %s, %s)
        """, (matricula, areaatuacao, curriculo, instituicao))
        conn.commit()
    finally:
        db.disconnect()

def update_professora(matricula, data):
    db = DatabaseConnection()
    conn = db.connect()
    try:
        cur = conn.cursor()
        cur.execute("""
            UPDATE Professora
            SET areaatuacao = %s, curriculo = %s, instituicao = %s
            WHERE matricula = %s
        """, (data['areaatuacao'], data['curriculo'], data['instituicao'], matricula))
        conn.commit()
    finally:
        db.disconnect()

def delete_professora(matricula):
    db = DatabaseConnection()
    conn = db.connect()
    try:
        cur = conn.cursor()
        cur.execute("DELETE FROM Professora WHERE matricula = %s", (matricula,))
        conn.commit()
    finally:
        db.disconnect()
