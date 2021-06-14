from logging import debug
from flask import Flask
from flask_restful import Api
from resources.universidade import Universidade, Curso

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///universidade.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)

@app.before_first_request
def cria_banco():
    banco.create_all()

api.add_resource(Universidade, '/cursos')
api.add_resource(Curso, '/cursos/<int:codigo>')

if __name__ ==  '__main__':
    from sql_alchemy import banco
    banco.init_app(app)
    app.run(debug=True)