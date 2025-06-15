from flask import Flask, jsonify, request
import psycopg2
import os

app = Flask(__name__)

def get_connection():
    return psycopg2.connect(
        host=os.environ["DB_HOST"],
        database=os.environ["DB_NAME"],
        user=os.environ["DB_USER"],
        password=os.environ["DB_PASSWORD"]
    )

@app.route("/hoteles", methods=["GET"])
def listar_hoteles():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS hoteles (id SERIAL PRIMARY KEY, nombre TEXT);")
    cur.execute("SELECT * FROM hoteles;")
    hoteles = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify(hoteles)

@app.route("/hoteles", methods=["POST"])
def agregar_hotel():
    data = request.get_json()
    nombre = data.get("nombre")
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO hoteles (nombre) VALUES (%s) RETURNING id;", (nombre,))
    hotel_id = cur.fetchone()[0]
    conn.commit()
    cur.close()
    conn.close()
    return jsonify({"id": hotel_id, "nombre": nombre}), 201

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
