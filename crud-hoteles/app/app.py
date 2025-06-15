from flask import Flask
import os
import psycopg2

app = Flask(__name__)

@app.route("/")
def index():
    try:
        conn = psycopg2.connect(
            host=os.environ["DB_HOST"],
            dbname=os.environ["DB_NAME"],
            user=os.environ["DB_USER"],
            password=os.environ["DB_PASSWORD"]
        )
        return "Conexión exitosa a la base de datos 🟢"
    except Exception as e:
        return f"Error de conexión ❌: {e}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
