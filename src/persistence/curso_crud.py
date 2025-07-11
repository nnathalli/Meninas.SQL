from db_connection.DatabaseConnection import DatabaseConnection
#from src.persistence.curso_crud import get_cursos, create_curso, update_curso, delete_curso

def get_cursos():
    db = DatabaseConnection()
    conn = db.connect()
    try:
        cur = conn.cursor()
        cur.execute("SELECT codcurso, nome, instituicao, departamento FROM Curso")
        rows = cur.fetchall()
        return [
            {
                "codcurso": row[0],
                "nome": row[1],
                "instituicao": row[2],
                "departamento": row[3]
            } for row in rows
        ]
    finally:
        db.disconnect()

def get_curso_por_codigo(codcurso):
    db = DatabaseConnection()
    conn = db.connect()
    try:
        cur = conn.cursor()
        cur.execute("SELECT codcurso, Nome, Instituicao, Departamento FROM Curso WHERE codcurso = %s", (codcurso,))
        row = cur.fetchone()
        if row:
            return {
                "codcurso": row[0],
                "nome": row[1],
                "instituicao": row[2],
                "departamento": row[3]
            }
        return None
    finally:
        db.disconnect()

# def create_curso(nome, instituicao, departamento):
#     db = DatabaseConnection()
#     conn = db.connect()
#     try:
#         cur = conn.cursor()
#         cur.execute(""""
#             INSERT INTO curso (nome, instituicao, departamento)
#             VALUES (%s, %s, %s)",
#         """, (nome, instituicao, departamento)
#         )
#         conn.commit()
#     finally:
#         db.disconnect()
def create_curso(data):
    db = DatabaseConnection()
    conn = db.connect()
    try:
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO curso (nome, instituicao, departamento) VALUES (%s, %s, %s)",
            (data["nome"], data["instituicao"], data["departamento"])
        )
        conn.commit()
    finally:
        db.disconnect()

def update_curso(codcurso, data):
    db = DatabaseConnection()
    conn = db.connect()
    try:
        cur = conn.cursor()
        cur.execute(
            "UPDATE Curso SET Nome = %s, Instituicao = %s, Departamento = %s WHERE codcurso = %s",
            (data["nome"], data["instituicao"], data["departamento"], codcurso)
        )
        conn.commit()
    finally:
        db.disconnect()

def delete_curso(codcurso):
    db = DatabaseConnection()
    conn = db.connect()
    try:
        cur = conn.cursor()
        cur.execute("DELETE FROM Curso WHERE codcurso = %s", (codcurso,))
        conn.commit()
    finally:
        db.disconnect()
