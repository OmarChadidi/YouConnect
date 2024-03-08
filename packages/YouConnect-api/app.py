from datetime import datetime

from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
import requests
import sqlite3
import uuid


app = Flask(__name__)

@app.route('/login', methods=['GET'])
def login():
    email = request.args.get('email')
    password = request.args.get('password')

    response = requests.post('https://api.youcan.shop/auth/login', json={'email': email, 'password': password})

    if response.status_code == 200:
        return 'Logged in successfully'
    else:
        return 'Invalid email or password', 401


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.sqlite'  # Replace with your database file path
db = SQLAlchemy(app)


class Profile(db.Model):
    __tablename__ = 'profiles'
    id = db.Column(db.Integer, primary_key=True)
    store_id = db.Column(db.String)
    logo = db.Column(db.String)
    name = db.Column(db.String)
    slug = db.Column(db.String)
    description = db.Column(db.String)
    social_media_links = db.Column(db.JSON)
    custom_links = db.Column(db.JSON)
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)
    deleted_at = db.Column(db.DateTime)

    def to_dict(self):
        return {
            'id': self.id,
            'store_id': self.store_id,
            'logo': self.logo,
            'name': self.name,
            'slug': self.slug,
            'description': self.description,
            'social_media_links': self.social_media_links,
            'custom_links': self.custom_links,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
            'deleted_at': self.deleted_at
        }


@app.route('/profiles', methods=['POST'])
def create_profile():
    data = request.get_json()
    connection = sqlite3.connect('data.sqlite')
    cursor = connection.cursor()

    new_profile_id = str(uuid.uuid4())

    name = data.get('name')
    slug = data.get('slug')
    logo = data.get('logo')
    store_id = data.get('store_id')
    description = data.get('description')
    social_media_links = json.dumps(data.get('social_media_links'))
    custom_links = json.dumps(data.get('custom_links'))
    created_at = datetime.now()
    updated_at = datetime.now()

    insert_query = "INSERT INTO profiles (id, name,store_id,slug,logo, description, social_media_links, custom_links, created_at, updated_at) VALUES (?, ?,?, ?, ?, ?,?,?,?,?)"
    cursor.execute(insert_query, (new_profile_id, name,store_id,slug,logo, description, social_media_links, custom_links,created_at, updated_at))

    connection.commit()
    connection.close()

    return jsonify({'message': 'Profile created successfully', 'profile_id': new_profile_id}), 201
@app.route('/profiles/<store_id>', methods=['GET'])
def get_profiles(store_id):
    connection = sqlite3.connect('data.sqlite')
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM profiles WHERE store_id = ?", (store_id,))
    results = cursor.fetchall()

    if results:
        profiles = []
        for result in results:
            profile = Profile(
                id=result[0],
                store_id=result[1],
                logo=result[2],
                name=result[3],
                slug=result[4],
                description=result[5],
                social_media_links=result[6],
                custom_links=result[7],
                created_at=result[8],
                updated_at=result[9],
                deleted_at=result[10]
            )
            profiles.append(profile.to_dict())

        return jsonify(profiles)
    else:
        return jsonify({'error': 'No profiles found for the specified store_id'}), 404
import json


@app.route('/profiles/<profile_id>', methods=['PUT'])
def edit_profile(profile_id):
    data = request.get_json()
    connection = sqlite3.connect('data.sqlite')
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM profiles WHERE id = ?", (profile_id,))
    result = cursor.fetchone()

    if result:
        set_clause = ''
        parameters = []

        for key, value in data.items():
            if key == 'social_media_links':
                value = json.dumps(value)
            set_clause += f"{key} = ?, "
            parameters.append(value)

        set_clause = set_clause[:-2]

        update_query = f"UPDATE profiles SET {set_clause} WHERE id = ?"
        parameters.append(profile_id)
        cursor.execute(update_query, parameters)

        connection.commit()
        connection.close()

        return jsonify({'message': 'Profile updated successfully'})
    else:
        connection.close()
        return jsonify({'error': 'Profile not found'}), 404

@app.route('/profiles/<profile_id>', methods=['DELETE'])
def delete_profile(profile_id):
    profile = Profile.query.get(profile_id)

    if profile:
        db.session.delete(profile)
        db.session.commit()
        return jsonify({'message': 'Profile deleted successfully'})
    else:
        return jsonify({'error': 'Profile not found'}), 404

if __name__ == '__main__':
    app.run()