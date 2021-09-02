from flask import Flask, jsonify, request
import json

app = Flask(__name__)

# carga inicial de tarefas
Tarefas = [
    {
        'descricao': 'Primeira tarefa'
    },
    {
        'descricao': 'Segunda tarefa'
    }
]

@app.route("/")
def home():
    return 'Esta funcionando :)'


@app.route("/tarefa/<int:id>", methods=['GET', 'PUT', 'DELETE'])
def desenvolvedor(id):
    # retorna uma tarefa
    if request.method == "GET":
        try:
            resposta = Tarefas[id]
        except IndexError:
            resposta = {'status':'erro', 'mensagem':'Tarefa nao encontrada'}
        return jsonify(resposta)

    # Atualiza uma tarefa
    elif request.method == "PUT":
        try:
            dados = json.loads(request.data)
            Tarefas[id] = dados
            mensagem = {'status': 'sucesso', 'mensagem':'Tarefa atualizado'}
        except IndexError:
            mensagem = {'status': 'erro', 'mensagem': 'Tarefa nao encontrada'}
        return jsonify(mensagem)

    # Deleta uma tarefa
    elif request.method == "DELETE":
        try:
            Tarefas.pop(id)
            mensagem = {'status': 'sucesso', 'mensagem': 'tarefa deletada'}
        except IndexError:
            mensagem = {'status': 'erro', 'mensagem': 'Tarefa não encontrada'}

        return jsonify(mensagem)


@app.route("/tarefa", methods=['POST','GET'])
def NovaTarefas():
    # retorna todas as tarefas
    if request.method == 'GET':
        return jsonify(Tarefas)

    # adiciona uma nova tarefa
    if request.method == "POST":
        dados = json.loads(request.data)
        Tarefas.append(dados)
        return jsonify({'status': 'sucesso', 'mensagem':'Registo inserido'})

if __name__ == '__main__':
    app.run(debug=True)
