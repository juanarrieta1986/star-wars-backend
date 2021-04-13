"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User
import flask

from models import db, User, Characters, Planets, Favorites
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_CONNECTION_STRING')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/user', methods=['GET'])
def handle_hello():

    response_body = {
        "msg": "Hello, this is your GET /user response "
    }

    return jsonify(response_body), 200

@app.route('/users/<int:user_id>/favorites', methods=['GET'])
def get_favorites(user_id):
    #todos.pop(position)
    return flask.jsonify("test string")

@app.route('/users/<int:user_id>/favorites', methods=['POST'])
def update_favorites(user_id):
    #todos.pop(position)
    return flask.jsonify("test string")

@app.route('/favorite/<int:favorite_id>', methods=['DELETE'])
def delete_favorites(favorite_id):
    #todos.pop(position)
    return flask.jsonify("test string")

@app.route('/people', methods=['GET'])
def get_characters():
    #todos.pop(position)
    user = Characters.query.get(id)
    return flask.jsonify(user)

@app.route('/people/<int:position>', methods=['GET'])
def get_individual_characters(position):
    #todos.pop(position)
    return flask.jsonify("test string")

@app.route('/planets', methods=['GET'])
def get_planets():
    #todos.pop(position)
    return flask.jsonify("test string")

@app.route('/planets/<int:position>', methods=['GET'])
def get_individual_planets(position):
    #todos.pop(position)
    return flask.jsonify("test string")

# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
