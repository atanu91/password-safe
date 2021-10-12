from flask import Flask, jsonify

password_safe_app = Flask(__name__)


@password_safe_app.route("/")
def say_hello():
    return "Hello World<br>This is the landing page"


@password_safe_app.route("/login", methods=["GET", "POST"])
def test():
    return jsonify("test")


@password_safe_app.route("/api")
def say2_hello():
    return jsonify("Hello World! This is the api landing page")


if __name__ == "__main__":
    password_safe_app.run(host='0.0.0.0', debug=True)
