import os
import psycopg2
from dotenv import load_dotenv
from flask import Flask, request, jsonify
import json


load_dotenv()


app = Flask(__name__)

# Connect to postgress database using psycopg and the env variable.
url = 'postgres://mydatabase_qd6z_user:F8joLE0vNlQeEoPZd4I2F56np3pQ6ppx@dpg-ck1l2ohgbqfc73ahann0-a/mydatabase_qd6z'
connection = psycopg2.connect(url)

# Create table using model
CREATE_TABLE = "CREATE TABLE IF NOT EXISTS persons(id serial PRIMARY KEY, name VARCHAR ( 100 ) UNIQUE NOT NULL)"
try:
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(CREATE_TABLE)
    connection.commit()
except:
    print("error: table could not be created!")


# setting home url to display welcome message
@app.route('/', methods=['GET'])
def home_url():
    return jsonify({"message": "Welcome! kindly use the api service"}), 200


# Create new person data
INSERT_INTO_PERSON = "INSERT INTO persons(name) VALUES (%s) RETURNING id;"


# Api endpoint to create new person data
@app.route('/api', methods=['POST'])
def create_person():
    """Fucntion that creates new person's data 
    and saves to db through api endpoint"""
    try:
        data = request.get_json()
        name = data['name']
        with connection:
            with connection.cursor() as cursor:
                cursor.execute(INSERT_INTO_PERSON, (name,))
                id = cursor.fetchone()[0]
        return {"id": id, "name": name, "message": f"{name} was created successfully!"}, 201
    except:
        return {"error": f"{name} failed to create"}, 500


# Api endpoint to retrieve all person data from db
SELECT_ALL_PERSON = "SELECT * FROM persons;"


@app.route('/api', methods=['GET'])
def get_all():
    """Send a GET request to retrieve all person data from db on api endpoint"""
    try:
        with connection:
            with connection.cursor() as cursor:
                cursor.execute(SELECT_ALL_PERSON)
                people = cursor.fetchall()
                if people:
                    result = []
                    for person in people:
                        result.append({"id": person[0], "name": person[1]})
                    return jsonify({"result": result})
                else:
                    return jsonify({"error": "person not found"}), 404
    except:
        return jsonify({"error": "Could not retrieve data!"}), 500


# Api endpoint to retrieve person data by id
@app.route('/api/<int:id>', methods=['GET'])
def get_person_by_id(id):
    """Retrieves person data by id on api endpoint"""
    try:
        with connection:
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM persons WHERE id = %s", (id,))
                person = cursor.fetchone()
                if person:
                    return jsonify({"id": person[0], "name": person[1]})
                else:
                    return jsonify({"error": f"person with id {id} not found"}), 404
    except:
        return jsonify({"error": f"id {id} could not be retrieved!"}), 500


# api endpoint to update person data by id
@app.route('/api/<int:id>', methods=['PUT'])
def update_person(id):
    """api endpoint to change person data by id"""
    try:
        data = request.get_json()
        name = data['name']
        with connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "UPDATE persons SET name = %s WHERE id = %s", (name, id,))
                if cursor.rowcount == 0:
                    return jsonify({"error": f"person with id {id} not found"}), 404
        return jsonify({"id": id, "name": name,
                        "message": f"person with id {id} has been updated successfully!"}), 200
    except:
        return jsonify({"error": "operation failed!"}), 500


# api endpoint to delete person data by id
@app.route('/api/<int:id>', methods=['DELETE'])
def delete_person(id):
    """Deletes person data by id on api endpoint"""
    try:
        with connection:
            with connection.cursor() as cursor:
                cursor.execute("DELETE FROM persons WHERE id = %s", (id,))
                if cursor.rowcount == 0:
                    return jsonify({"error": f"person with id {id} not found"}), 404
        return jsonify({"message": f"person with id {id} has been deleted successfully!"}), 200
    except:
        return jsonify({"error": "operation failed!"})

if __name__ == "__main__":
    app.run()