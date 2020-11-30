from flask import Flask, jsonify, request
from personajes import personajes


app = Flask(__name__)


@app.route('/personajes')
def getPersonajes():
    return jsonify({'personajes' : personajes})


@app.route('/personajes/<int:id>')
def getPersonaje(id):
    personaje_encontrado = [personaje for personaje in personajes if personaje['id'] == id ]
    if personaje_encontrado:
        return jsonify({'name' : personaje_encontrado})
    else:
        return jsonify({'message': 'personaje not found'})


@app.route('/personajes', methods=['POST'])
def addPersonaje():
    new_personaje = {
        "id" : request.json['id'],
        "name" : request.json['name'],
        "category" : request.json['category'],
        "arma" : request.json['arma']
    }
    personajes.append(new_personaje)

    return jsonify({"message": "personaje agregado", "personajes": personajes})


@app.route('/personajes/<string:personaje_name>', methods=['PUT'])
def editPersonaje(personaje_name):
    personaje_encontrado = [personaje for personaje in personajes if personaje['name']== personaje_name]
    if personaje_encontrado:
        personaje_encontrado[0]['name'] = request.json['name']
        personaje_encontrado[0]['category'] = request.json['category']
        personaje_encontrado[0]['arma'] = request.json['arma']
        personaje_encontrado[0]['id'] = request.json['id']
        return jsonify({'meesage': 'personaje actualizado', 'personaje': personaje_encontrado})


if __name__ == "__main__":
    app.run (debug=True, port = 4000)
