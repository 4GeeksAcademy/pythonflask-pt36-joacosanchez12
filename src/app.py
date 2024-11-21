from flask import Flask, jsonify, request
app = Flask(__name__)
todos = [
   { "label": "My first task", "done": False },
    { "label": "My second task", "done": False }
]
@app.route('/todos', methods=['GET'])
def hello_world():
    return jsonify(todos)

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json
    todos.append(request_body)
    return jsonify(todos), 200

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    todos.pop(position-1)
    return jsonify(todos), 200

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)