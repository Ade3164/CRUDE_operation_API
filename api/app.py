from flask import Flask, jsonify, request
import mysql.connector
from config import DATABASE_CONFIG  

app = Flask(__name__)

db = mysql.connector.connect(**DATABASE_CONFIG)
cursor = db.cursor()

@app.route("/api/persons", methods=["GET"])
def get_persons():
    cursor.execute("SELECT id, name FROM persons")
    persons_data = cursor.fetchall()
    persons_list = [{"id": id, "name": name} for id, name in persons_data]
    return jsonify(persons_list)

@app.route("/api/persons/<person_identifier>", methods=["GET"])
def get_person(person_identifier):
    # Check if person_identifier is numeric (ID) or alphanumeric (Name)
    if person_identifier.isdigit():
        query = "SELECT id, name FROM persons WHERE id = %s"
    else:
        query = "SELECT id, name FROM persons WHERE name = %s"
    
    cursor.execute(query, (person_identifier,))
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
