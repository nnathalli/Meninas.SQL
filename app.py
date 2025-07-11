from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from src.persistence.integrante_crud import (
    get_integrantes, get_integrante_por_matricula,
    create_integrante, update_integrante, delete_integrante
)
from src.persistence.frente_crud import (
    get_frentes, get_frente_por_codigo,
    create_frente, update_frente, delete_frente
)
from src.persistence.atividade_crud import (
    get_atividades, get_atividade_por_codigo,
    create_atividade, update_atividade, delete_atividade
)
from src.persistence.professora_crud import (
    get_professoras, get_professora_por_matricula,
    create_professora, update_professora, delete_professora
)
from src.persistence.aluna_crud import (
    get_alunas, get_aluna_por_matricula,
    create_aluna, update_aluna, delete_aluna
)
from src.persistence.integrante_frente_crud import (
    associar_integrante_frente, desassociar_integrante_frente,
    get_integrantes_por_frente
)
from src.persistence.integrante_atividade_crud import (
    associar_integrante_atividade, desassociar_integrante_atividade,
    get_integrantes_por_atividade
)

# from src.persistence.curso_crud import (
#     get_cursos, get_curso_por_codigo,
#     create_curso, update_curso, delete_curso
# )
# from src.persistence.curso_crud import get_cursos, get_curso_por_codigo, create_curso, update_curso, delete_curso


app = Flask(__name__, static_folder='frontend', static_url_path='')
CORS(app)
@app.route('/')
def serve_html():
    return send_from_directory(app.static_folder, 'frontend.html')

# ---------- INTEGRANTES ----------
@app.route('/api/integrantes', methods=['GET'])
def listar_integrantes():
    return jsonify(get_integrantes()), 200

@app.route('/api/integrantes/<matricula>', methods=['GET'])
def obter_integrante(matricula):
    integrante = get_integrante_por_matricula(matricula)
    return jsonify(integrante or {'erro': 'Não encontrado'}), 200

@app.route('/api/integrantes', methods=['POST'])
def adicionar_integrante():
    try:
        data = request.get_json()
        matricula = data['matricula']
        nome = data['nome']
        datanasc = data['datanasc']
        dataentrada = data['dataentrada']
        email = data['email']
        telefone = data['telefone']

        create_integrante(matricula, nome, datanasc, dataentrada, email, telefone)


        return jsonify({'mensagem': 'Integrante cadastrado com sucesso'}), 201
    except Exception as e:
        return jsonify({'erro': str(e)}), 400

@app.route('/api/integrantes/<matricula>', methods=['PUT'])
def editar_integrante(matricula):
    data = request.get_json()
    update_integrante(matricula, data)
    return jsonify({'mensagem': 'Integrante atualizado'}), 200

@app.route('/api/integrantes/<matricula>', methods=['DELETE'])
def excluir_integrante(matricula):
    delete_integrante(matricula)
    return jsonify({'mensagem': 'Integrante excluído'}), 200

# ---------- ALUNAS ----------
@app.route('/api/alunas', methods=['GET'])
def listar_alunas():
    return jsonify(get_alunas()), 200

@app.route('/api/alunas/<matricula>', methods=['GET'])
def obter_aluna(matricula):
    aluna = get_aluna_por_matricula(matricula)
    return jsonify(aluna or {'erro': 'Não encontrada'}), 200

@app.route('/api/alunas', methods=['POST'])
def adicionar_aluna():
    try:
        data = request.get_json()
        create_aluna(
            data['matricula'],
            data['bolsa'],
            data['codcurso']
        )
        return jsonify({'mensagem': 'Aluna cadastrada com sucesso'}), 201
    except Exception as e:
        return jsonify({'erro': str(e)}), 400


@app.route('/api/alunas/<matricula>', methods=['PUT'])
def editar_aluna(matricula):
    try:
        data = request.get_json()
        update_aluna(matricula, data)
        return jsonify({'mensagem': 'Aluna atualizada'}), 200
    except Exception as e:
        return jsonify({'erro': str(e)}), 400

@app.route('/api/alunas/<matricula>', methods=['DELETE'])
def excluir_aluna(matricula):
    try:
        delete_aluna(matricula)
        return jsonify({'mensagem': 'Aluna excluída'}), 200
    except Exception as e:
        return jsonify({'erro': str(e)}), 400

# ---------- PROFESSORAS ----------

@app.route('/api/professoras', methods=['GET'])
def listar_professoras():
    return jsonify(get_professoras()), 200

@app.route('/api/professoras/<matricula>', methods=['GET'])
def obter_professora(matricula):
    prof = get_professora_por_matricula(matricula)
    return jsonify(prof or {'erro': 'Não encontrada'}), 200

@app.route('/api/professoras', methods=['POST'])
def adicionar_professora():
    try:
        data = request.get_json()
        matricula = data['matricula']
        areaatuacao = data['areaatuacao']
        curriculo = data['curriculo']
        instituicao = data['instituicao']
        
        create_professora(matricula, areaatuacao, curriculo, instituicao)

        return jsonify({'mensagem': 'Professora cadastrada com sucesso'}), 201
    except Exception as e:
        print("Erro ao cadastrar professora:", e)
        return jsonify({'erro': str(e)}), 400

@app.route('/api/professoras/<matricula>', methods=['PUT'])
def editar_professora(matricula):
    try:
        data = request.get_json()
        update_professora(matricula, data)
        return jsonify({'mensagem': 'Professora atualizada'}), 200
    except Exception as e:
        return jsonify({'erro': str(e)}), 400

@app.route('/api/professoras/<matricula>', methods=['DELETE'])
def excluir_professora(matricula):
    try:
        delete_professora(matricula)
        return jsonify({'mensagem': 'Professora excluída'}), 200
    except Exception as e:
        return jsonify({'erro': str(e)}), 400

# ---------- FRENTES ----------
@app.route('/api/frentes', methods=['GET'])
def listar_frentes():
    return jsonify(get_frentes()), 200

@app.route('/api/frentes/<codigo>', methods=['GET'])
def obter_frente(codigo):
    frente = get_frente_por_codigo(codigo)
    return jsonify(frente or {'erro': 'Não encontrado'}), 200

@app.route('/api/frentes', methods=['POST'])
def adicionar_frente():
    try:
        data = request.get_json()
        codigo = data['codigo']
        nome = data['nome']
        tipo = data['tipo']
        descricao = data['descricao']
        datacriacao = data['datacriacao']

        create_frente(codigo, nome, tipo, descricao, datacriacao)

        return jsonify({'mensagem': 'Frente criada'}), 201
    except Exception as e:
        return jsonify({'erro': str(e)}), 400


@app.route('/api/frentes/<codigo>', methods=['PUT'])
def editar_frente(codigo):
    data = request.get_json()
    update_frente(codigo, data)
    return jsonify({'mensagem': 'Frente atualizada'}), 200

@app.route('/api/frentes/<codigo>', methods=['DELETE'])
def excluir_frente(codigo):
    delete_frente(codigo)
    return jsonify({'mensagem': 'Frente excluída'}), 200


# ---------- ATIVIDADES ----------
@app.route('/api/atividades', methods=['GET'])
def listar_atividades():
    return jsonify(get_atividades()), 200

@app.route('/api/atividades/<codigo>', methods=['GET'])
def obter_atividade(codigo):
    atividade = get_atividade_por_codigo(codigo)
    return jsonify(atividade or {'erro': 'Não encontrado'}), 200

@app.route('/api/atividades', methods=['POST'])
def adicionar_atividade():
    try:
        data = request.get_json()
        codigo = data['codigo']
        nome = data ['nome']
        descricao = data ['descricao']
        tipo = data ['tipo']
        local = data ['local']
        data_hora = data ['data_hora']
        duracao = data ['duracao']

        create_atividade(codigo, nome, descricao, tipo, local, data_hora, duracao)

        return jsonify({'mensagem': 'Atividade criada'}), 201
    except Exception as e:
        return jsonify({'erro': str(e)}), 400


@app.route('/api/atividades/<codigo>', methods=['PUT'])
def editar_atividade(codigo):
    data = request.get_json()
    update_atividade(codigo, data)
    return jsonify({'mensagem': 'Atividade atualizada'}), 200

@app.route('/api/atividades/<codigo>', methods=['DELETE'])
def excluir_atividade(codigo):
    delete_atividade(codigo)
    return jsonify({'mensagem': 'Atividade excluída'}), 200

# ---------- CURSOS ----------

from src.persistence.curso_crud import (
    get_cursos,
    get_curso_por_codigo,
    create_curso,
    update_curso,
    delete_curso
)

@app.route("/api/cursos", methods=["GET"])
def listar_cursos():
    return jsonify(get_cursos()), 200

@app.route("/api/cursos/<int:codcurso>", methods=["GET"])
def obter_curso(codcurso):
    curso = get_curso_por_codigo(codcurso)
    if curso:
        return jsonify(curso), 200
    return jsonify({"erro": "Curso não encontrado"}), 404

@app.route("/api/cursos", methods=["POST"])
def adicionar_curso():
    try:
        data = request.get_json()
        create_curso(data)
        return jsonify({"mensagem": "Curso criado com sucesso"}), 201
    except Exception as e:
        return jsonify({"erro": str(e)}), 400

@app.route("/api/cursos/<int:codcurso>", methods=["PUT"])
def editar_curso(codcurso):
    try:
        data = request.get_json()
        update_curso(codcurso, data)
        return jsonify({"mensagem": "Curso atualizado com sucesso"}), 200
    except Exception as e:
        return jsonify({"erro": str(e)}), 400

@app.route("/api/cursos/<int:codcurso>", methods=["DELETE"])
def excluir_curso(codcurso):
    try:
        delete_curso(codcurso)
        return jsonify({"mensagem": "Curso excluído com sucesso"}), 200
    except Exception as e:
        return jsonify({"erro": str(e)}), 400
# ---------- INTEGRANTE FRENTE ----------
@app.route('/api/frentes/<codigo>/integrantes', methods=['GET'])
def listar_integrantes_frente(codigo):
    return jsonify(get_integrantes_por_frente(codigo)), 200

@app.route('/api/frentes/<codigo>/integrantes', methods=['POST'])
def adicionar_integrante_frente(codigo):
    try:
        data = request.get_json()
        associar_integrante_frente(data['matricula'], codigo, data.get('funcao', 'Participante'))
        return jsonify({'mensagem': 'Integrante associado à frente com sucesso'}), 201
    except Exception as e:
        return jsonify({'erro': str(e)}), 400

@app.route('/api/frentes/<codigo>/integrantes/<matricula>', methods=['DELETE'])
def remover_integrante_frente(codigo, matricula):
    try:
        # Verifica se o integrante existe
        integrante = get_integrante_por_matricula(matricula)
        if not integrante:
            return jsonify({'erro': 'Integrante não encontrado'}), 404
            
        # Verifica se a frente existe
        frente = get_frente_por_codigo(codigo)
        if not frente:
            return jsonify({'erro': 'Frente não encontrada'}), 404
            
        # Tenta desassociar
        sucesso = desassociar_integrante_frente(matricula, codigo)
        
        if sucesso:
            return jsonify({'mensagem': 'Integrante desassociado da frente'}), 200
        else:
            return jsonify({'erro': 'Associação não encontrada ou já desativada'}), 404
            
    except Exception as e:
        return jsonify({'erro': str(e)}), 500

# ---------- INTEGRANTE ATIVIDADE ----------
@app.route('/api/atividades/<codigo>/integrantes', methods=['GET'])
def listar_integrantes_atividade(codigo):
    return jsonify(get_integrantes_por_atividade(codigo)), 200

@app.route('/api/atividades/<codigo>/integrantes', methods=['POST'])
def adicionar_integrante_atividade(codigo):
    try:
        data = request.get_json()
        associar_integrante_atividade(data['matricula'], codigo)
        return jsonify({'mensagem': 'Integrante associado à atividade com sucesso'}), 201
    except Exception as e:
        return jsonify({'erro': str(e)}), 400

@app.route('/api/atividades/<codigo>/integrantes/<matricula>', methods=['DELETE'])
def remover_integrante_atividade(codigo, matricula):
    try:
        desassociar_integrante_atividade(matricula, codigo)
        return jsonify({'mensagem': 'Integrante desassociado da atividade'}), 200
    except Exception as e:
        return jsonify({'erro': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)