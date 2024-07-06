from flask import Flask, jsonify, request
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required, JWTManager
from authentication import check_credentials
from operations import get_expenses
app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "secretkey"
jwt = JWTManager(app)
@app.route("/login")
def login():
    username = request.json.get("username")
    password = request.json.get("password")
    checked = check_credentials(username,password)
    if checked is True:
        token = create_access_token(identity=username)
        return jsonify({"token":token}),200
    elif checked is False:
        return jsonify({"status":"false"}),300
@app.route("/operations")
def operations():
    data = get_expenses()
    return jsonify(data)
if __name__ == "__main__":
    app.run(debug=True)
