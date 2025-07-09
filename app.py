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
        data_nasc = data['data_nasc']
        data_entrada = data['data_entrada']
        email = data['email']
        telefone = data['telefone']

        create_integrante(matricula, nome, data_nasc, data_entrada, email, telefone)

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


if __name__ == '__main__':
    app.run(debug=True)
