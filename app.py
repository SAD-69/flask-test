from flask import Flask, request, jsonify

app = Flask(__name__)

# Lista de livros
livros = [
    {"id": 1, "titulo": "Livro 1", "autor": "Autor 1"},
    {"id": 2, "titulo": "Livro 2", "autor": "Autor 2"},
    {"id": 3, "titulo": "Livro 3", "autor": "Autor 3"}
]

@app.route('/livros', methods=['GET'])
def listar_livros():
    return jsonify(livros)

@app.route('/livros/<int:livro_id>', methods=['GET'])
def obter_livro(livro_id):
    livro = next((livro for livro in livros if livro['id'] == livro_id), None)
    if livro:
        return jsonify(livro)
    else:
        return jsonify({"mensagem": "Livro não encontrado"}), 404

@app.route('/livros', methods=['POST'])
def adicionar_livro():
    data = request.get_json()
    novo_livro = {
        "id": len(livros) + 1,
        "titulo": data['titulo'],
        "autor": data['autor']
    }
    livros.append(novo_livro)
    return jsonify(novo_livro), 201

@app.route('/livros/<int:livro_id>', methods=['PUT'])
def atualizar_livro(livro_id):
    livro = next((livro for livro in livros if livro['id'] == livro_id), None)
    if livro:
        data = request.get_json()
        livro['titulo'] = data['titulo']
        livro['autor'] = data['autor']
        return jsonify(livro)
    else:
        return jsonify({"mensagem": "Livro não encontrado"}), 404

@app.route('/livros/<int:livro_id>', methods=['DELETE'])
def excluir_livro(livro_id):
    global livros
    livros = [livro for livro in livros if livro['id'] != livro_id]
    return jsonify({"mensagem": "Livro excluído com sucesso"}), 200

if __name__ == '__main__':
    app.run(debug=True)
