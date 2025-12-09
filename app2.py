from flask import Flask, jsonify, request
from flask_cors import CORS
import mysql.connector

app = Flask(__name__)
CORS(app)

db_config = {
    'host':'localhost',
    'user':'root',
    'password':'root',
    'database':'abc'
}

def get_db_connection():
    return mysql.connector.connect(**db_config)

@app.route('/')
def home():
    return jsonify({"message":"Welcome to app"})

@app.route('/api/users', methods = ['GET'])
def get_user():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor = cursor.execute("SELCT * FROM users")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(rows)


if __name__ == '__main__':
    app.run(debug = True)
