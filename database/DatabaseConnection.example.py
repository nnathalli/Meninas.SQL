import psycopg2

def get_connection():
    return psycopg2.connect(
        host="SEU_HOST",
        database="NOME_BANCO",
        user="SEU_USUARIO",
        password="SUA_SENHA"
    )
