from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, ForeignKey, Integer, String

db = SQLAlchemy()

#class User(db.Model):
#    id = db.Column(db.Integer, primary_key=True)
#    email = db.Column(db.String(120), unique=True, nullable=False)
#    password = db.Column(db.String(80), unique=False, nullable=False)
#    is_active = db.Column(db.Boolean(), unique=False, nullable=False)


class User(db.Model):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    password = db.Column(db.String(250), nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }

class Characters(db.Model):
    __tablename__ = 'characters'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250),  nullable=False)
    height = db.Column(db.String(250),  nullable=False)
    mass = db.Column(db.String(250),  nullable=False)
    hair_color = db.Column(db.String(250),  nullable=False)
    skin_color = db.Column(db.String(250),  nullable=False)
    eye_color = db.Column(db.String(250),  nullable=False)
    birth_year = db.Column(db.String(250),  nullable=False)
    gender = db.Column(db.String(250),  nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            # do not serialize the password, its a security breach
        }
    
    def get_all_chars():
        all_chars = Characters.query.all()
        all_chars = list(map(lambda x: x.serialize(), all_chars))
        return all_chars
    
    def get_one_char(position):
        one_char = Characters.query.filter_by(id = position)
        one_char = list(map(lambda x: x.serialize(), one_char))
        return one_char


class Planets(db.Model):
    __tablename__ = 'planets'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250),  nullable=False)
    rotation_period = db.Column(db.String(250),  nullable=False)
    orbital_period = db.Column(db.String(250),  nullable=False)
    diameter = db.Column(db.String(250),  nullable=False)
    climate = db.Column(db.String(250),  nullable=False)
    gravity = db.Column(db.String(250),  nullable=False)
    terrain = db.Column(db.String(250),  nullable=False)
    surface_water = db.Column(db.String(250),  nullable=False)
    population = db.Column(db.String(250),  nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            # do not serialize the password, its a security breach
        }

    def get_all_planets():
        all_planets = Planets.query.all()
        all_planets = list(map(lambda x: x.serialize(), all_planets))
        return all_planets

class Favorites(db.Model):
    __tablename__ = 'favorites'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = db.Column(db.Integer, primary_key=True)
    userId = db.Column(db.Integer, ForeignKey('user.id'))
    charId = db.Column(db.Integer,  ForeignKey('characters.id'))
    planetId = db.Column(db.Integer,  ForeignKey('planets.id'))

    def serialize(self):
        return {
            "charId": self.charId,
            "planetId": self.planetId,
            # do not serialize the password, its a security breach
        }

    def get_favorites():
        favorites = Favorites.query.all()
        favorites = list(map(lambda x: x.serialize(), favorites))
        return favorites