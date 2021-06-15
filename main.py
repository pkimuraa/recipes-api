from flask import Flask

app = Flask(__name__)

@app.route("/recipe", methods=['GET', 'POST'])
def recipe():
    return "Oi meu amor"