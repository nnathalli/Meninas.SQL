from db_connection.DatabaseConnection import DatabaseConnection

def associar_integrante_frente(matricula, codigo_frente, funcao="Participante"):
    db = DatabaseConnection()
    conn = db.connect()
    try:
        cur = conn.cursor()
        cur.execute("""
            INSERT INTO integrantefrente (matricula, codigofrente, funcao, dt_inicio, dt_fim)
            VALUES (%s, %s, %s, CURRENT_DATE, NULL)
        """, (matricula, codigo_frente, funcao))
        conn.commit()
    finally:
        db.disconnect()

def desassociar_integrante_frente(matricula, codigo_frente):
    db = DatabaseConnection()
    conn = db.connect()
    try:
        cur = conn.cursor()
        
        # Verifica se existe associação ativa
        cur.execute("""
            SELECT 1 FROM integrantefrente 
            WHERE matricula = %s AND codigofrente = %s AND dt_fim IS NULL
            FOR UPDATE  -- Bloqueia o registro para evitar concorrência
        """, (matricula, codigo_frente))
        
        if not cur.fetchone():
            return False
            
        # Atualiza com data de fim
        cur.execute("""
            UPDATE integrantefrente 
            SET dt_fim = CURRENT_DATE
            WHERE matricula = %s AND codigofrente = %s AND dt_fim IS NULL
            RETURNING 1  -- Retorna 1 se atualizou algo
        """, (matricula, codigo_frente))
        
        conn.commit()
        return cur.fetchone() is not None
        
    except Exception as e:
        conn.rollback()
        print(f"Erro ao desassociar integrante: {e}")
        return False
    finally:
        db.disconnect()

def get_integrantes_por_frente(codigo_frente):
    db = DatabaseConnection()
    conn = db.connect()
    try:
        cur = conn.cursor()
        cur.execute("""
            SELECT i.matricula, i.nome, inf.funcao, inf.dt_inicio
            FROM integrante i
            JOIN integrantefrente inf ON i.matricula = inf.matricula
            WHERE inf.codigofrente = %s AND inf.dt_fim IS NULL
        """, (codigo_frente,))
        return [{'matricula': r[0], 'nome': r[1], 'funcao': r[2], 'dt_inicio': str(r[3])} for r in cur.fetchall()]
    finally:
        db.disconnect()