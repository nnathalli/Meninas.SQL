import psycopg2

class DatabaseConnection:
    def __init__(self):
        self.conn = None

    def connect(self):
        try:
            self.conn = psycopg2.connect(
                host="localhost",
                port=5432,
                dbname="seu_banco",
                user="seu_usuario",
                password="sua_senha"
            )
            return self.conn
        except Exception as e:
            print("Erro na conexão com o banco:", e)
            return None

    def disconnect(self):
        if self.conn:
            self.conn.close()
