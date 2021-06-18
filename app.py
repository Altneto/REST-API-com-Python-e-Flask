from logging import debug
from flask import Flask
from flask_restful import Api
from resources.curso import Cursos, Curso
from resources.aluno import Alunos, Aluno
from resources.matricula import Matriculas, Matricula

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///universidade.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)

@app.before_first_request
def cria_banco():
    banco.create_all()

api.add_resource(Cursos, '/cursos')
api.add_resource(Alunos, '/alunos')
api.add_resource(Curso, '/cursos/<int:codigo>')
api.add_resource(Aluno, '/alunos/<int:matricula>')
api.add_resource(Matriculas, '/matriculas')
api.add_resource(Matricula, '/matriculas/<int:matricula>,<int:codigo_curso>')

if __name__ ==  '__main__':
    from sql_alchemy import banco
    banco.init_app(app)
    app.run(debug=True)