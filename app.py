from flask import Flask, send_from_directory, render_template_string
import os

app = Flask(__name__)

# 1️⃣ Rota principal para servir o FrontEnd.html
@app.route('/')
def index():
    frontend_path = os.path.join(os.getcwd(), 'frontend')
    with open(os.path.join(frontend_path, 'FrontEnd.html'), 'r', encoding='utf-8') as f:
        content = f.read()
    return render_template_string(content)

# 2️⃣ Rota para servir o script.js
@app.route('/script.js')
def serve_script():
    return send_from_directory('frontend', 'script.js')

# 3️⃣ (Opcional) Endpoint de teste
@app.route('/ping')
def ping():
    return "✅ Backend Flask rodando e servindo o Meninas.SQL"

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, request, jsonify
from flask_cors import CORS
from database.database import get_db_connection, create_tables
import json
from datetime import datetime, timedelta

app = Flask(__name__)
CORS(app) # Habilita CORS para todas as rotas, permitindo que o frontend acesse

# Garante que as tabelas existam ao iniciar a aplicação
create_tables()

# --- Rotas para Integrantes ---

@app.route('/integrantes', methods=['GET'])
def get_integrantes():
    """
    Retorna uma lista de todos os integrantes no banco de dados.
    """
    conn = get_db_connection()
    if conn is None:
        return jsonify({"error": "Falha na conexão com o banco de dados"}), 500
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT Matricula, Nome, DataNasc, DataEntrada, Email, Telefone FROM Integrante")
        integrantes = cursor.fetchall()
        # Formata os resultados para JSON
        integrantes_list = []
        for intg in integrantes:
            integrantes_list.append({
                "matricula": intg[0],
                "nome": intg[1],
                "dataNasc": intg[2].strftime('%Y-%m-%d') if intg[2] else None,
                "dataEntrada": intg[3].strftime('%Y-%m-%d') if intg[3] else None,
                "email": intg[4],
                "telefone": intg[5]
            })
        return jsonify(integrantes_list), 200
    except Exception as e:
        conn.rollback()
        return jsonify({"error": str(e)}), 500
    finally:
        cursor.close()
        conn.close()

@app.route('/integrantes', methods=['POST'])
def add_integrante():
    """
    Adiciona um novo integrante ao banco de dados.
    Espera um JSON com os dados do integrante.
    """
    data = request.get_json()
    if not data:
        return jsonify({"error": "Dados JSON ausentes"}), 400

    matricula = data.get('matricula')
    nome = data.get('nome')
    data_nasc = data.get('dataNasc')
    data_entrada = data.get('dataEntrada')
    email = data.get('email')
    telefone = data.get('telefone')

    if not all([matricula, nome, email]):
        return jsonify({"error": "Matrícula, Nome e Email são campos obrigatórios"}), 400

    conn = get_db_connection()
    if conn is None:
        return jsonify({"error": "Falha na conexão com o banco de dados"}), 500
    try:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO Integrante (Matricula, Nome, DataNasc, DataEntrada, Email, Telefone) VALUES (%s, %s, %s, %s, %s, %s)",
            (matricula, nome, data_nasc, data_entrada, email, telefone)
        )
        conn.commit()
        return jsonify({"message": "Integrante adicionado com sucesso!"}), 201
    except psycopg2.IntegrityError as e:
        conn.rollback()
        if "duplicate key value violates unique constraint" in str(e):
            return jsonify({"error": "Matrícula ou Email já existem."}), 409
        return jsonify({"error": str(e)}), 500
    except Exception as e:
        conn.rollback()
        return jsonify({"error": str(e)}), 500
    finally:
        cursor.close()
        conn.close()

@app.route('/integrantes/<string:matricula>', methods=['PUT'])
def update_integrante(matricula):
    """
    Atualiza um integrante existente no banco de dados pela matrícula.
    Espera um JSON com os dados atualizados do integrante.
    """
    data = request.get_json()
    if not data:
        return jsonify({"error": "Dados JSON ausentes"}), 400

    nome = data.get('nome')
    data_nasc = data.get('dataNasc')
    data_entrada = data.get('dataEntrada')
    email = data.get('email')
    telefone = data.get('telefone')

    conn = get_db_connection()
    if conn is None:
        return jsonify({"error": "Falha na conexão com o banco de dados"}), 500
    try:
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE Integrante SET Nome = %s, DataNasc = %s, DataEntrada = %s, Email = %s, Telefone = %s WHERE Matricula = %s",
            (nome, data_nasc, data_entrada, email, telefone, matricula)
        )
        conn.commit()
        if cursor.rowcount == 0:
            return jsonify({"message": "Integrante não encontrado."}), 404
        return jsonify({"message": "Integrante atualizado com sucesso!"}), 200
    except psycopg2.IntegrityError as e:
        conn.rollback()
        if "duplicate key value violates unique constraint" in str(e):
            return jsonify({"error": "Email já existe para outro integrante."}), 409
        return jsonify({"error": str(e)}), 500
    except Exception as e:
        conn.rollback()
        return jsonify({"error": str(e)}), 500
    finally:
        cursor.close()
        conn.close()

@app.route('/integrantes/<string:matricula>', methods=['DELETE'])
def delete_integrante(matricula):
    """
    Exclui um integrante do banco de dados pela matrícula.
    """
    conn = get_db_connection()
    if conn is None:
        return jsonify({"error": "Falha na conexão com o banco de dados"}), 500
    try:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM Integrante WHERE Matricula = %s", (matricula,))
        conn.commit()
        if cursor.rowcount == 0:
            return jsonify({"message": "Integrante não encontrado."}), 404
        return jsonify({"message": "Integrante excluído com sucesso!"}), 200
    except Exception as e:
        conn.rollback()
        return jsonify({"error": str(e)}), 500
    finally:
        cursor.close()
        conn.close()

# --- Rotas para FrentesDeTrabalho ---

@app.route('/frentes', methods=['GET'])
def get_frentes():
    """
    Retorna uma lista de todas as frentes de trabalho.
    """
    conn = get_db_connection()
    if conn is None:
        return jsonify({"error": "Falha na conexão com o banco de dados"}), 500
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT Codigo, Nome, Tipo, Descricao, DataCriacao FROM FrentesDeTrabalho")
        frentes = cursor.fetchall()
        frentes_list = []
        for f in frentes:
            frentes_list.append({
                "codigo": f[0],
                "nome": f[1],
                "tipo": f[2],
                "descricao": f[3],
                "dataCriacao": f[4].strftime('%Y-%m-%d') if f[4] else None
            })
        return jsonify(frentes_list), 200
    except Exception as e:
        conn.rollback()
        return jsonify({"error": str(e)}), 500
    finally:
        cursor.close()
        conn.close()

@app.route('/frentes', methods=['POST'])
def add_frente():
    """
    Adiciona uma nova frente de trabalho.
    """
    data = request.get_json()
    if not data:
        return jsonify({"error": "Dados JSON ausentes"}), 400

    nome = data.get('nome')
    tipo = data.get('tipo')
    descricao = data.get('descricao')
    data_criacao = data.get('dataCriacao')

    if not all([nome, tipo, data_criacao]):
        return jsonify({"error": "Nome, Tipo e Data de Criação são campos obrigatórios"}), 400

    conn = get_db_connection()
    if conn is None:
        return jsonify({"error": "Falha na conexão com o banco de dados"}), 500
    try:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO FrentesDeTrabalho (Nome, Tipo, Descricao, DataCriacao) VALUES (%s, %s, %s, %s) RETURNING Codigo",
            (nome, tipo, descricao, data_criacao)
        )
        new_codigo = cursor.fetchone()[0]
        conn.commit()
        return jsonify({"message": "Frente de trabalho adicionada com sucesso!", "codigo": new_codigo}), 201
    except Exception as e:
        conn.rollback()
        return jsonify({"error": str(e)}), 500
    finally:
        cursor.close()
        conn.close()

@app.route('/frentes/<int:codigo>', methods=['PUT'])
def update_frente(codigo):
    """
    Atualiza uma frente de trabalho existente.
    """
    data = request.get_json()
    if not data:
        return jsonify({"error": "Dados JSON ausentes"}), 400

    nome = data.get('nome')
    tipo = data.get('tipo')
    descricao = data.get('descricao')
    data_criacao = data.get('dataCriacao')

    conn = get_db_connection()
    if conn is None:
        return jsonify({"error": "Falha na conexão com o banco de dados"}), 500
    try:
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE FrentesDeTrabalho SET Nome = %s, Tipo = %s, Descricao = %s, DataCriacao = %s WHERE Codigo = %s",
            (nome, tipo, descricao, data_criacao, codigo)
        )
        conn.commit()
        if cursor.rowcount == 0:
            return jsonify({"message": "Frente de trabalho não encontrada."}), 404
        return jsonify({"message": "Frente de trabalho atualizada com sucesso!"}), 200
    except Exception as e:
        conn.rollback()
        return jsonify({"error": str(e)}), 500
    finally:
        cursor.close()
        conn.close()

@app.route('/frentes/<int:codigo>', methods=['DELETE'])
def delete_frente(codigo):
    """
    Exclui uma frente de trabalho.
    """
    conn = get_db_connection()
    if conn is None:
        return jsonify({"error": "Falha na conexão com o banco de dados"}), 500
    try:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM FrentesDeTrabalho WHERE Codigo = %s", (codigo,))
        conn.commit()
        if cursor.rowcount == 0:
            return jsonify({"message": "Frente de trabalho não encontrada."}), 404
        return jsonify({"message": "Frente de trabalho excluída com sucesso!"}), 200
    except Exception as e:
        conn.rollback()
        return jsonify({"error": str(e)}), 500
    finally:
        cursor.close()
        conn.close()

# --- Rotas para Atividades ---

@app.route('/atividades', methods=['GET'])
def get_atividades():
    """
    Retorna uma lista de todas as atividades.
    """
    conn = get_db_connection()
    if conn is None:
        return jsonify({"error": "Falha na conexão com o banco de dados"}), 500
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT Codigo, Nome, Descricao, Tipo, Local, DataHora, Duracao FROM Atividades")
        atividades = cursor.fetchall()
        atividades_list = []
        for act in atividades:
            atividades_list.append({
                "codigo": act[0],
                "nome": act[1],
                "descricao": act[2],
                "tipo": act[3],
                "local": act[4],
                "dataHora": act[5].isoformat() if act[5] else None, # Formato ISO para datetime-local
                "duracao": str(act[6]) if act[6] else None # Intervalo como string
            })
        return jsonify(atividades_list), 200
    except Exception as e:
        conn.rollback()
        return jsonify({"error": str(e)}), 500
    finally:
        cursor.close()
        conn.close()

@app.route('/atividades', methods=['POST'])
def add_atividade():
    """
    Adiciona uma nova atividade.
    """
    data = request.get_json()
    if not data:
        return jsonify({"error": "Dados JSON ausentes"}), 400

    nome = data.get('nome')
    descricao = data.get('descricao')
    tipo = data.get('tipo')
    local = data.get('local')
    data_hora_str = data.get('dataHora')
    duracao_str = data.get('duracao')

    if not all([nome, tipo, local, data_hora_str, duracao_str]):
        return jsonify({"error": "Nome, Tipo, Local, Data e Hora, e Duração são campos obrigatórios"}), 400

    conn = get_db_connection()
    if conn is None:
        return jsonify({"error": "Falha na conexão com o banco de dados"}), 500
    try:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO Atividades (Nome, Descricao, Tipo, Local, DataHora, Duracao) VALUES (%s, %s, %s, %s, %s, %s) RETURNING Codigo",
            (nome, descricao, tipo, local, data_hora_str, duracao_str)
        )
        new_codigo = cursor.fetchone()[0]
        conn.commit()
        return jsonify({"message": "Atividade adicionada com sucesso!", "codigo": new_codigo}), 201
    except Exception as e:
        conn.rollback()
        return jsonify({"error": str(e)}), 500
    finally:
        cursor.close()
        conn.close()

@app.route('/atividades/<int:codigo>', methods=['PUT'])
def update_atividade(codigo):
    """
    Atualiza uma atividade existente.
    """
    data = request.get_json()
    if not data:
        return jsonify({"error": "Dados JSON ausentes"}), 400

    nome = data.get('nome')
    descricao = data.get('descricao')
    tipo = data.get('tipo')
    local = data.get('local')
    data_hora_str = data.get('dataHora')
    duracao_str = data.get('duracao')

    conn = get_db_connection()
    if conn is None:
        return jsonify({"error": "Falha na conexão com o banco de dados"}), 500
    try:
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE Atividades SET Nome = %s, Descricao = %s, Tipo = %s, Local = %s, DataHora = %s, Duracao = %s WHERE Codigo = %s",
            (nome, descricao, tipo, local, data_hora_str, duracao_str, codigo)
        )
        conn.commit()
        if cursor.rowcount == 0:
            return jsonify({"message": "Atividade não encontrada."}), 404
        return jsonify({"message": "Atividade atualizada com sucesso!"}), 200
    except Exception as e:
        conn.rollback()
        return jsonify({"error": str(e)}), 500
    finally:
        cursor.close()
        conn.close()

@app.route('/atividades/<int:codigo>', methods=['DELETE'])
def delete_atividade(codigo):
    """
    Exclui uma atividade.
    """
    conn = get_db_connection()
    if conn is None:
        return jsonify({"error": "Falha na conexão com o banco de dados"}), 500
    try:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM Atividades WHERE Codigo = %s", (codigo,))
        conn.commit()
        if cursor.rowcount == 0:
            return jsonify({"message": "Atividade não encontrada."}), 404
        return jsonify({"message": "Atividade excluída com sucesso!"}), 200
    except Exception as e:
        conn.rollback()
        return jsonify({"error": str(e)}), 500
    finally:
        cursor.close()
        conn.close()

# --- Rotas para Dashboard e Maratonas (Somente Leitura - Views) ---

@app.route('/dashboard', methods=['GET'])
def get_dashboard_data():
    """
    Retorna dados para o dashboard gerencial (simulando view_dashboard_gerencial).
    """
    conn = get_db_connection()
    if conn is None:
        return jsonify({"error": "Falha na conexão com o banco de dados"}), 500
    try:
        cursor = conn.cursor()
        # Esta é uma consulta simplificada. Idealmente, você usaria sua view real.
        cursor.execute("""
            SELECT
                ft.Nome,
                ft.Tipo,
                COUNT(DISTINCT i.Matricula) AS TotalIntegrantes,
                STRING_AGG(DISTINCT i.Nome, ', ') AS NomesIntegrantes,
                COUNT(DISTINCT a.Codigo) AS TotalAtividades,
                MAX(a.DataHora) AS UltimaAtividade,
                ep.Nome AS EscolaParceira
            FROM FrentesDeTrabalho ft
            LEFT JOIN IntegranteFrente ift ON ft.Codigo = ift.CodigoFrente
            LEFT JOIN Integrante i ON ift.Matricula = i.Matricula
            LEFT JOIN IntegranteAtividade ia ON i.Matricula = ia.Matricula
            LEFT JOIN Atividades a ON ia.CodigoAtividade = a.Codigo
            LEFT JOIN FrenteEscola fe ON ft.Codigo = fe.CodigoFrente
            LEFT JOIN EscolasParceiras ep ON fe.CodigoEscola = ep.Codigo
            GROUP BY ft.Codigo, ft.Nome, ft.Tipo, ep.Nome
            ORDER BY ft.Nome;
        """)
        dashboard_data = cursor.fetchall()
        dashboard_list = []
        for row in dashboard_data:
            dashboard_list.append({
                "nomeFrente": row[0],
                "tipo": row[1],
                "totalIntegrantes": row[2],
                "nomesIntegrantes": row[3],
                "totalAtividades": row[4],
                "ultimaAtividade": row[5].strftime('%Y-%m-%d') if row[5] else None,
                "escolaParceira": row[6]
            })
        return jsonify(dashboard_list), 200
    except Exception as e:
        conn.rollback()
        return jsonify({"error": str(e)}), 500
    finally:
        cursor.close()
        conn.close()

@app.route('/maratonas', methods=['GET'])
def get_maratonas_data():
    """
    Retorna dados das maratonas (simulando view_maratonas).
    """
    conn = get_db_connection()
    if conn is None:
        return jsonify({"error": "Falha na conexão com o banco de dados"}), 500
    try:
        cursor = conn.cursor()
        # Esta é uma consulta simplificada. Idealmente, você usaria sua view real.
        cursor.execute("""
            SELECT
                mp.Nome,
                mp.Edicao,
                mp.Premiacao,
                COUNT(DISTINCT eq.Id_equipe) AS TotalEquipes,
                COUNT(DISTINCT pe.IdParticipante) AS TotalParticipantes,
                STRING_AGG(DISTINCT eq.NomeEquipe, ', ') AS NomesEquipes,
                STRING_AGG(DISTINCT em.Classificacao || ' (' || eq.NomeEquipe || ')', '; ') AS Classificacoes,
                (SELECT json_agg(json_build_object('enunciado', p.Enunciado, 'edicao', p.Edicao))
                 FROM Perguntas p WHERE p.CodigoMaratona = mp.Codigo) AS PerguntasJson
            FROM MaratonaProg mp
            LEFT JOIN EquipeMaratona em ON mp.Codigo = em.CodigoMaratona
            LEFT JOIN Equipe eq ON em.Id_equipe = eq.Id_equipe
            LEFT JOIN ParticipanteEquipe pe ON eq.Id_equipe = pe.Id_equipe
            GROUP BY mp.Codigo, mp.Nome, mp.Edicao, mp.Premiacao
            ORDER BY mp.Nome;
        """)
        maratonas_data = cursor.fetchall()
        maratonas_list = []
        for row in maratonas_data:
            maratonas_list.append({
                "nomeMaratona": row[0],
                "edicao": row[1],
                "premiacao": row[2],
                "totalEquipes": row[3],
                "totalParticipantes": row[4],
                "nomesEquipes": row[5],
                "classificacao": row[6],
                "perguntasJson": json.loads(row[7]) if row[7] else [] # Converte a string JSON para objeto Python
            })
        return jsonify(maratonas_list), 200
    except Exception as e:
        conn.rollback()
        return jsonify({"error": str(e)}), 500
    finally:
        cursor.close()
        conn.close()


if __name__ == '__main__':
    # Executa o servidor Flask na porta 5000
    # O debug=True permite recarregamento automático em mudanças de código
    # e fornece informações de depuração.
    app.run(debug=True, port=5000)
