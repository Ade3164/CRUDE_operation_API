import os
from flask import Flask, jsonify, request
import mysql.connector
from dotenv import load_dotenv

# Load environmental variables from .env
load_dotenv()

# Load database configuration from environmental variables
DB_HOST = os.environ.get("DB_HOST")
DB_PORT = os.environ.get("DB_PORT")
DB_USER = os.environ.get("DB_USER")
DB_PASSWORD = os.environ.get("DB_PASSWORD")
DB_NAME = os.environ.get("DB_NAME")

# Initialize the Flask application
app = Flask(__name__)

# Create the database connection
db = mysql.connector.connect(
    host=DB_HOST,
    port=DB_PORT,
    user=DB_USER,
    password=DB_PASSWORD,
    database=DB_NAME
)

cursor = db.cursor()

# Function to create the "persons" table if it doesn't exist
def create_persons_table():
    create_table_query = """
    CREATE TABLE IF NOT EXISTS persons (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255) NOT NULL
    )
    """
    cursor.execute(create_table_query)
    db.commit()

# Call the function to create the table
create_persons_table()

# Function to insert initial data into the "persons" table
def insert_initial_data():
    insert_data_query = """
    INSERT INTO persons (name) VALUES (%s)
    """
    data = [("Alice",), ("Bob",), ("Charlie",)]
    cursor.executemany(insert_data_query, data)
    db.commit()

# Call the function to insert initial data
insert_initial_data()

@app.route('/', methods=['GET'])
def home():
  return "Welcome HNG CRUD operation /api"

@app.route("/api/persons", methods=["GET"])
def get_persons():
    cursor.execute("SELECT id, name FROM persons")
    persons_data = cursor.fetchall()
    persons_list = [{"id": id, "name": name} for id, name in persons_data]
    return jsonify(persons_list)

@app.route("/api/persons/<int:id>", methods=["GET"])
def get_person(id):
    cursor.execute("SELECT id, name FROM persons WHERE id = %s", (id,))
    person_data = cursor.fetchone()
    if person_data:
        return jsonify({"id": person_data[0], "name": person_data[1]})
    else:
        return jsonify({"error": "Person not found"}), 404

@app.route("/api/persons/<string:name>", methods=["GET"])
def get_person_by_name(name):
    cursor.execute("SELECT id, name FROM persons WHERE name = %s", (name,))
    person_data = cursor.fetchone()
    if person_data:
        return jsonify({"id": person_data[0], "name": person_data[1]})
    else:
        return jsonify({"error": "Person not found"}), 404

@app.route("/api/persons", methods=["POST"])
def create_person():
    data = request.get_json()
    name = data.get("name")
    if name is None:
        return jsonify({"error": "Name is required"}), 400

    cursor.execute("SELECT id FROM persons WHERE name = %s", (name,))
    existing_person = cursor.fetchone()
    if existing_person:
        return jsonify({"error": "Person with the same name already exists"}), 400

    cursor.execute("INSERT INTO persons (name) VALUES (%s)", (name,))
    db.commit()
    new_id = cursor.lastrowid

    return jsonify({"id": new_id, "name": name}), 201

@app.route("/api/persons/<int:id>", methods=["PUT"])
def update_person(id):
    data = request.get_json()
    name = data.get("name")
    if name is None:
        return jsonify({"error": "Name is required"}), 400

    cursor.execute("SELECT id FROM persons WHERE id = %s", (id,))
    existing_person = cursor.fetchone()
    if not existing_person:
        return jsonify({"error": "Person not found"}), 404

    cursor.execute("UPDATE persons SET name = %s WHERE id = %s", (name, id))
    db.commit()

    return jsonify({"id": id, "name": name})

@app.route("/api/persons/<int:id>", methods=["DELETE"])
def delete_person(id):
    cursor.execute("SELECT id FROM persons WHERE id = %s", (id,))
    existing_person = cursor.fetchone()
    if not existing_person:
        return jsonify({"error": "Person not found"}), 404

    cursor.execute("DELETE FROM persons WHERE id = %s", (id,))
    db.commit()

    return jsonify({"message": "Person deleted"}), 200

if __name__ == "__main__":
    app.run(debug=True)
