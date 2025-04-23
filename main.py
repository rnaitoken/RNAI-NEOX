from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "¡La bestia RNAI está viva en Vercel!"

if __name__ == "__main__":
    app.run()
