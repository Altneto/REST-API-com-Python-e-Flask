from flask_restful import Resource, reqparse
from models.aluno import AlunoModel

class Alunos(Resource):
   def get(self):
        return {'alunos': [aluno.json() for aluno in AlunoModel.query.all()]}

class Aluno(Resource):
    artefatos = reqparse.RequestParser()
    artefatos.add_argument('nome', type=str, required = True, help="O campo nome do aluno não pode ficar vazio")

    def get(self, matricula):
        aluno = AlunoModel.find_Aluno(matricula)
        if aluno:
            return aluno.json()
        else:
            return {'Erro': 'Matricula não encontrada.'}, 404

    def post(self, matricula):
        if AlunoModel.find_Aluno(matricula):
            return {'Aviso': 'Aluno já cadastrado'}, 400
        dados_Aluno = Aluno.artefatos.parse_args()
        aluno = AlunoModel(matricula, **dados_Aluno)
        try:
            aluno.add_Aluno()
        except:
            return {'Aviso': 'Erro na inclusão do aluno'}, 500
        else:
            return aluno.json()

    def put(self, matricula):
        dados_Aluno = Aluno.artefatos.parse_args()
        aluno_Encontrado = AlunoModel.find_Aluno(matricula)
        if aluno_Encontrado:
            aluno_Encontrado.update_Aluno(**dados_Aluno)
            aluno_Encontrado.add_Aluno()
            return aluno_Encontrado.json(), 200
        aluno = AlunoModel(matricula, **dados_Aluno)
        try:
            aluno.add_Aluno()
        except:
            return {'Aviso': 'Erro ao atualizar o Aluno.'}, 500
        return aluno.json(), 201

    def delete(self, matricula):
        aluno = AlunoModel.find_Aluno(matricula)
        if aluno:
            try:
                aluno.delete_Aluno()
            except:
                return {'Aviso': 'Erro ao deletar o Aluno.'}, 500
            else:
                return {'Aviso': 'Aluno deletado.'}, 200
        else:
            return {'Erro': 'Codigo de matricula invalido.'}, 404