import psycopg2

def get_connection():
    return psycopg2.connect(
        host="localhost",
        database="Meninas.SQL",
        user="postgres",
        password="eastw1nd"
    )
