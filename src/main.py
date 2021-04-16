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
from models import db, User, Characters, Planets, Favorites
import flask

#import JWT for tokenization
from flask_jwt_extended import JWTManager, jwt_required, get_jwt_identity, create_access_token

#from models import db, User, Characters, Planets, Favorites
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_CONNECTION_STRING')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# config for jwt
app.config["JWT_SECRET_KEY"] = os.environ.get("JWT_SECRET_KEY")
jwt = JWTManager(app)

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
    return jsonify(Favorites.get_favorites(user_id))

@app.route('/users/<int:user_id>/favorites', methods=['POST'])
def update_favorites(user_id):
    char_id = request.json.get("charID", None)
    planet_id = request.json.get("planetID", None)
    fav_type = request.json.get("entityType", None)
    #user_ID,char_ID,planet_ID,fav_type
    return jsonify(Favorites.add_favorite(user_id, char_id, planet_id, fav_type))

@app.route('/favorite/<int:favorite_id>', methods=['DELETE'])
@jwt_required()
def delete_favorites(favorite_id):
    current_id = get_jwt_identity()
    user = Favorites.query.get(favorite_id)
    return jsonify(Favorites.delete_favorite(favorite_id))
    #return "ok"

@app.route('/people', methods=['GET'])
def get_characters():
    return jsonify(Characters.get_all_chars())

@app.route('/people/<int:position>', methods=['GET'])
def get_individual_characters(position):
    return jsonify(Characters.get_one_char(position))

@app.route('/planets', methods=['GET'])
def get_planets():
    #todos.pop(position)
    return jsonify(Planets.get_all_planets())

@app.route('/planets/<int:position>', methods=['GET'])
def get_individual_planets(position):
    return jsonify(Planets.get_one_planet(position))

@app.route('/login', methods=['POST']) 
def login():
    email = request.json.get("name", None)
    password = request.json.get("password", None)

    # valida si estan vacios los ingresos
    if email is None:
        return jsonify({"msg": "No email was provided"}), 400
    if password is None:
        return jsonify({"msg": "No password was provided"}), 400

    # para proteger contraseñas usen hashed_password
    # busca usuario en BBDD
    user = User.query.filter_by(name=email, password=password).first()
    if user is None:
        return jsonify({"msg": "Invalid username or password"}), 401
    else:
        # crear token
        my_token = create_access_token(identity=user.id)
        return jsonify({"token": my_token})
    
@app.route('/register', methods=['POST'])
def register_user():
    email = request.json.get("name", None)
    password = request.json.get("password", None)

    # valida si estan vacios los ingresos
    if email is None:
        return jsonify({"msg": "No email was provided"}), 400
    if password is None:
        return jsonify({"msg": "No password was provided"}), 400
    
    # busca usuario en BBDD
    user = User.query.filter_by(name=email).first()
    if user:
        # the user was not found on the database
        return jsonify({"msg": "User already exists"}), 401
    else:
        # crea usuario nuevo
        create_user
        # crea registro nuevo en BBDD de 
        return jsonify({"msg": "User created successfully"}), 200

# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
