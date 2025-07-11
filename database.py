from db_connection.DatabaseConnection import get_connection
import psycopg2
from psycopg2 import Error
import os

def get_db_connection():
    """
    Estabelece e retorna uma conexão com o banco de dados PostgreSQL.
    As credenciais são carregadas de variáveis de ambiente ou padrões.
    """
    try:
        conn = psycopg2.connect(
            user=os.getenv("DB_USER", "postgres"),          # Usuário do banco de dados
            password=os.getenv("DB_PASSWORD", "eastw1nd"),     # Senha do banco de dados
            host=os.getenv("DB_HOST", "localhost"),         # Host do banco de dados
            port=os.getenv("DB_PORT", "5432"),              # Porta do banco de dados
            database=os.getenv("DB_NAME", "Meninas.SQL")    # Nome do banco de dados
        )
        print("Conexão com o banco de dados estabelecida com sucesso!")
        return conn
    except Error as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return None

# Função para criar as tabelas se não existirem
def create_tables():
    """
    Cria as tabelas necessárias no banco de dados se elas ainda não existirem.
    Isso é útil para garantir que o esquema esteja pronto para uso.
    """
    conn = get_db_connection()
    if conn:
        try:
            cursor = conn.cursor()
            # Script SQL para criar as tabelas
            # Adapte este script para o seu schema.sql completo,
            # incluindo todas as tabelas e relacionamentos.
            # Este é um exemplo simplificado para as tabelas CRUD principais.
            schema_sql = """
            CREATE TABLE IF NOT EXISTS Integrante (
                Matricula VARCHAR(20) PRIMARY KEY,
                Nome VARCHAR(100) NOT NULL,
                Email VARCHAR(100) UNIQUE NOT NULL,
                Telefone VARCHAR(20)
            );

            CREATE TABLE IF NOT EXISTS FrentesDeTrabalho (
                Codigo SERIAL PRIMARY KEY,
                Nome VARCHAR(100) NOT NULL,
                Tipo VARCHAR(50),
                Descricao TEXT,
                DataCriacao DATE
            );

            CREATE TABLE IF NOT EXISTS Atividades (
                Codigo SERIAL PRIMARY KEY,
                Nome VARCHAR(100) NOT NULL,
                Descricao TEXT,
                Tipo VARCHAR(50),
                Local VARCHAR(100),
                DataHora TIMESTAMP,
                Duracao INTERVAL
            );
            """
            cursor.execute(schema_sql)
            conn.commit()
            print("Tabelas verificadas/criadas com sucesso.")
        except Error as e:
            print(f"Erro ao criar tabelas: {e}")
            conn.rollback()
        finally:
            cursor.close()
            conn.close()

# Se este script for executado diretamente, ele tentará criar as tabelas
if __name__ == "__main__":
    create_tables()
    # Exemplo de uso da conexão
    conn = get_db_connection()
    if conn:
        conn.close()


def listar_integrantes():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM integrante")
    colnames = [desc[0] for desc in cur.description]
    resultados = [dict(zip(colnames, row)) for row in cur.fetchall()]
    cur.close()
    conn.close()
    return resultados

def cadastrar_integrante(data):
    print("Dados recebidos:", data)
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("CALL cadastro_integrante(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (
        data['matricula'],
        data['nome'],
        # data['dataNasc'],
        # data['dataEntrada'],
        data['email'],
        data['telefone'],
        data['tipo'],
        json.dumps(data.get('extra', {})),
        data.get('codigoFrente', None),
        data.get('funcao', 'Participante'),
        data.get('associarAtividades', False)
    ))

    conn.commit()
    cur.close()
    conn.close()
