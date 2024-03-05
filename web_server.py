from flask import Flask, render_template
from flask_restful import Api, Resource
from db_class import DB
from main import *
app = Flask(__name__)
api = Api()


class Main(Resource):
    def get(self, name):
        if name == 'count_box':
            return my_bd.view_box()
        elif name == 'count_paper':
            return  my_bd.view_paper()

api.add_resource(Main, '/<name>')
api.init_app(app)
@app.route("/")
def index():
    count_all = my_bd.viev_all()
    return render_template('index.html', count_all = count_all )
