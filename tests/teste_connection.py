from database.DatabaseConnection import DatabaseConnection

def testar_conexao():
    """Testa a conexão com o banco de dados e verifica tabelas essenciais"""
    print("\n=== Iniciando teste de conexão ===")
    
    # 1. Testar conexão básica
    db = DatabaseConnection()
    conn = db.connect()
    
    if not conn:
        print("❌ Falha na conexão com o banco de dados")
        return False
    
    print("✅ Conexão estabelecida com sucesso")
    
    # 2. Verificar tabelas essenciais
    tabelas_esperadas = {'integrante', 'frentesdetrabalho', 'atividades'}
    cur = conn.cursor()
    
    try:
        cur.execute("""
            SELECT table_name 
            FROM information_schema.tables 
            WHERE table_schema = 'public'
        """)
        tabelas_existentes = {row[0] for row in cur.fetchall()}
        
        # Verifica se todas as tabelas esperadas existem
        faltantes = tabelas_esperadas - tabelas_existentes
        if faltantes:
            print(f"❌ Tabelas faltando: {faltantes}")
            return False
        
        print(f"✅ Tabelas essenciais presentes: {tabelas_esperadas}")
        
        # 3. Teste de consulta básica
        cur.execute("SELECT COUNT(*) FROM integrante")
        count = cur.fetchone()[0]
        print(f"Total de integrantes registrados: {count}")
        
        return True
        
    except Exception as e:
        print(f"❌ Erro durante verificação: {str(e)}")
        return False
    finally:
        cur.close()
        conn.close()

if __name__ == "__main__":
    testar_conexao()
