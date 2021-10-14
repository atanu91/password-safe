import json
from flask import Flask, jsonify, request
from src.backend.functions.validateRegistration import validate_user_registration

password_safe_api = Flask(__name__)


@password_safe_api.route("/api")
def say_hello():
    return jsonify("Hello World! This is the api landing page")


@password_safe_api.route("/api/create", methods=['POST'])
def user_create():
    input_user_data = dict(json.loads(request.data))
    # input_user_name = input_user_data['user_name']
    # input_user_password = input_user_data['password']
    validate_user_registration(input_user_data['user_name'], input_user_data['password'])


@password_safe_api.route("/api/update")
def user_update():
    return jsonify("Hello World! This is the api landing page")


@password_safe_api.route("/api/{user_hash}/delete")
def user_delete():
    return jsonify("Hello World! This is the api landing page")


@password_safe_api.route("/api/{user_hash}/reset")
def user_reset():
    return jsonify("Hello World! This is the api landing page")


if __name__ == "__main__":
    password_safe_api.run(host='0.0.0.0', debug=True)
