from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return jsonify({"message": "Hello from Flask!", "status": "ok"})


@app.route("/about")
def about():
    return jsonify({"app": "Flask Learning App", "version": "1.0", "author": "Mario"})


if __name__ == "__main__":
    app.run(debug=True)
