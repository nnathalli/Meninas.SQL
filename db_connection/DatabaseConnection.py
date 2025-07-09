import psycopg2

class DatabaseConnection:
    def __init__(self):
        self.conn = None

    def connect(self):
        try:
            self.conn = psycopg2.connect(
                host="localhost",
                port=5432,               
                dbname="Meninas.SQL",    
                user="postgres",      
                password="eastw1nd"
            )
            return self.conn
        except Exception as e:
            print("Erro na conexão com o banco:", e)
            return None

    def disconnect(self):
        if self.conn:
            self.conn.close()

def get_connection():
    return DatabaseConnection().connect()

