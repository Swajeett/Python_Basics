from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
import mysql.connector
import bcrypt

app = Flask(__name__)
CORS(app)

# --------------------------
# JWT Configuration
# --------------------------
app.config['JWT_SECRET_KEY'] = 'super-secret-key'  # change in production!
jwt = JWTManager(app)

# --------------------------
# MySQL Configuration
# --------------------------
db_config = {
    'host': 'localhost',
    'user': 'root',        # your MySQL username
    'password': '',        # your MySQL password
    'database': 'flask_api_demo'
}

def get_db_connection():
    return mysql.connector.connect(**db_config)

# --------------------------
# User Registration
# --------------------------
@app.route('/api/register', methods=['POST'])
def register():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    password = data.get('password')

    if not all([name, email, password]):
        return jsonify({"error": "Missing fields"}), 400

    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO users (name, email, password) VALUES (%s, %s, %s)",
                       (name, email, hashed_password))
        conn.commit()
        return jsonify({"message": "User registered successfully"}), 201
    except mysql.connector.Error as err:
        return jsonify({"error": str(err)}), 500
    finally:
        cursor.close()
        conn.close()

# --------------------------
# User Login
# --------------------------
@app.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
    user = cursor.fetchone()
    cursor.close()
    conn.close()

    if not user:
        return jsonify({"error": "User not found"}), 404

    if bcrypt.checkpw(password.encode('utf-8'), user['password'].encode('utf-8')):
        access_token = create_access_token(identity=user['id'])
        return jsonify({
            "message": "Login successful",
            "token": access_token
        })
    else:
        return jsonify({"error": "Invalid password"}), 401

# --------------------------
# Protected Profile Route
# --------------------------
@app.route('/api/profile', methods=['GET'])
@jwt_required()
def profile():
    current_user_id = get_jwt_identity()
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT id, name, email FROM users WHERE id = %s", (current_user_id,))
    user = cursor.fetchone()
    cursor.close()
    conn.close()

    if not user:
        return jsonify({"error": "User not found"}), 404
    return jsonify(user)

# --------------------------
# Test Public Route
# --------------------------
@app.route('/')
def home():
    return jsonify({"message": "Welcome to the JWT Secured Flask API!"})

# --------------------------
# Run Server
# --------------------------
if __name__ == '__main__':
    app.run(debug=True)
