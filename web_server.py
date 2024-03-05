from flask import Flask
from flask_restful import Api, Resource
app = Flask(__name__)
api = Api()
@app.route("/")
def hello():
    return "Helllo, ROME"

