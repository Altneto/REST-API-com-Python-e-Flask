from flask_restful import Resource, reqparse
from models.matricula import MatriculaModel

class Matriculas(Resource):
   def get(self):
        return {'matriculas': [matricula.json() for matricula in MatriculaModel.query.all()]}

class Matricula(Resource):
    atributos = reqparse.RequestParser()
    atributos.add_argument('frequencia', type=str)
    atributos.add_argument('media', type=float)

    def get(self, matricula):
        matricula =  MatriculaModel.find_matricula(matricula)
        if matricula:
            return matricula.json()
        return{'Erro': 'Matricula não encontrada.'}, 404
    
    def post(self, matricula, codigo_curso):
        if MatriculaModel.find_codigo(codigo_curso) and MatriculaModel.find_matricula(matricula):
            return {'Aviso': 'Curso já cadastrado'}, 400
        dados = Matricula.atributos.parse_args()
        matricula = MatriculaModel(matricula, codigo_curso, **dados)
        try:
            matricula.save_matricula()
        except:
            return {'mensagem': 'Erro interno na inclusão da matricula'}, 500
        return matricula.json()

    def delete(self, matricula, codigo_curso):
        if MatriculaModel.find_codigo(codigo_curso):
            matricula = MatriculaModel.find_matricula(matricula)
            if matricula:
                try:
                    matricula.delete_matricula(matricula)
                except:
                    {'mensagem': 'Erro interno ao tentar deletar a matricula.'}, 500
                return {'mensagem': 'Matricula deletado.'}, 200
            return {'Erro': 'Matricula invalida.'}, 404
        return {'Erro': 'Codigo de curso invalido.'}, 404
        