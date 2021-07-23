import requests

import flask
from flask import request

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/searchgame', methods=['GET'])
def searchGame():
    if 'game' in request.args:
        game = request.args['game']
    else:
        return "Error: No game is provided. Please specify an game."
    url = 'https://www.giantbomb.com/api/search/?'

    query = {'api_key': '5d9ae9e568351525765958236c41c028d2736eed', 'format': 'json', 'resources': 'game',
             'query': '%22'+game+'%22'}

    response = requests.get(url, params=query, headers={'user-agent': 'test-user'})
    return response.json()


app.run()
