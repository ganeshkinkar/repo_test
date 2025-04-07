from flask import Flask, request, jsonify

app = Flask(__name__)

USERS = {
    "admin": "secret123",
    "user": "password"
}

@app.route("/login", methods=["POST"])def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return jsonify({"error": "Username and password required"}), 400

    if USERS.get(username) == password:
        return jsonify({"message": "Login successful"}), 200
    else:
        return jsonify({"error": "Invalid credentials"}), 401

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5006)