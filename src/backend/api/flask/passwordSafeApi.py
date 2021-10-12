from flask import Flask, jsonify

password_safe_api = Flask(__name__)


@password_safe_api.route("/api")
def say_hello():
    return jsonify("Hello World! This is the api landing page")


@password_safe_api.route("/api/create")
def user_create():
    return jsonify("Hello World! This is the api landing page")


@password_safe_api.route("/api/update")
def user_update():
    return jsonify("Hello World! This is the api landing page")


@password_safe_api.route("/api/{user_hash}/delete")
def user_delete():
    return jsonify("Hello World! This is the api landing page")


@password_safe_api.route("/api/{user_hash}/reset")
def user_delete():
    return jsonify("Hello World! This is the api landing page")


if __name__ == "__main__":
    password_safe_api.run(host='0.0.0.0', debug=True)
