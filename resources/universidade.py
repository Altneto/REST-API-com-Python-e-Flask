from flask_restful import Resource, reqparse
from models.curso import CursoModel

class Universidade(Resource):
    def get(self):
        return {'cursos': [curso.json() for curso in CursoModel.query.all()]}

class Curso(Resource):
    atributos = reqparse.RequestParser()
    atributos.add_argument('nome', type=str, required=True, help="O campo 'nome' não pode ficar vazio")

    def get(self, codigo):
        curso = CursoModel.find_curso(codigo)
        if curso:
            return curso.json()
        return{'Erro': 'Curso não encontrado.'}, 404
    
    def post(self, codigo):
        if CursoModel.find_curso(codigo):
            return {'mensagem': 'Curso já adicionado'}, 400
        dados = Curso.atributos.parse_args()
        curso = CursoModel(codigo, **dados)
        try:
            curso.save_curso()
        except:
            return {'mensagem': 'Erro interno na inclusão do curso'}, 500
        return curso.json()

    def put(self, codigo):
        dados = Curso.atributos.parse_args()
        curso_encontrado = CursoModel.find_curso(codigo)
        if curso_encontrado:
            curso_encontrado.update_curso(**dados)
            curso_encontrado.save_curso()
            return curso_encontrado.json(), 200
        curso = CursoModel(codigo, **dados)
        try:
            curso.save_curso()
        except:
            return {'mensagem': 'Erro interno na inclusão do curso'}, 500
        return curso.json(), 201

    def delete(self, codigo):
        curso = CursoModel.find_curso(codigo)
        if curso:
            try:
                curso.delete_curso()
            except:
                {'mensagem': 'Erro interno ao tentar deletar o curso.'}, 500
            return {'mensagem': 'Curso deletado.'}, 200
        return {'Erro': 'Codigo de curso invalido.'}, 404
           