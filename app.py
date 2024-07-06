from flask import Flask, jsonify, request
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required, JWTManager
from authentication import check_credentials
from operations import get_expenses, get_income, insert_values
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
@jwt_required
@app.route("/operations",methods=["POST"])
def operations():
    operation = request.json.get("operation")
    if operation == None:
        return get_expenses()
    elif operation == "expenses_daily":
        return get_expenses("daily")
    elif operation == "expenses_monthly":
        return get_expenses("monthly")
    elif operation == "income_daily":
        return get_income("daily")
    elif operation == "income_monthly":
        return get_income("monthly")
    elif operation == "insert_value_income":
        id = request.json.get("id")
        date = request.json.get("date")
        note = request.json.get("note")
        amount = request.json.get("amount")
        return insert_values(id,date,note,amount,"income")
    elif operation == "insert_value_expenses":
        id = request.json.get("id")
        date = request.json.get("date")
        note = request.json.get("note")
        amount = request.json.get("amount")
        return insert_values(id,date,note,amount,"expenses")
    else:
        return 400
if __name__ == "__main__":
    app.run(debug=True)
