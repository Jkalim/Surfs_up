from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello World"

@app.route("/sports")
def sports():
    return "Olympic Basketball"

if __name__ == "__main__":
    app.run()

