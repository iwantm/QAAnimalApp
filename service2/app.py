from flask import Flask, Response, request, jsonify
import random

animals = {
    'bear': 'roar',
    'bee': 'buzz',
    'tiger': 'roar',
    'lion': 'roar',
    'cat': 'meow',
    'chicken': 'cluck',
    'cow': 'moo',
    'dog': 'bark',
    'duck': 'quack',
    'frog': 'ribbit',
    'goose': 'honk',
    'horse': 'neigh',
    'mouse': 'squeak',
    'owl': 'hoot',
    'pig': 'Oink',
    'sheep': 'baa',
    'snake': 'hiss',
    'turkey': 'gobble'
}

app = Flask(__name__)


@app.route('/animal', methods=['GET'])
def random_animal():
    animal = random.choice(list(animals.keys())).capitalize()
    return jsonify({"animal": animal})


@app.route('/animal/sound', methods=['POST'])
def animal_sound():
    animal = request.get_json()['animal'].lower()
    sound = animals.get(animal)
    return jsonify({"sound": sound})


if __name__ == '__main__':
    app.run(debug=True, port=5001, host='0.0.0.0')
