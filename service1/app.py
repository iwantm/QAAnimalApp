from flask import Flask, jsonify, request, render_template
import requests


import random

app = Flask(__name__)
api = "http://service2:5001"


@app.route('/')
def index():
    request = requests.get(api+'/animal')
    animal = request.json()['animal']
    sound_request = requests.post(
        api + '/animal/sound', json={"animal": animal})
    sound = sound_request.json()['sound']
    return render_template('index.html', animal=animal, sound=sound)


if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')
