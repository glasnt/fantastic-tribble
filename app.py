from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return "👋 glasnt/fantastic-tribble!"


if __name__ == "__main__":
    app.run(host="localhost", port=8080, debug=True)
