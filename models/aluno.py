from sql_alchemy import banco

class AlunoModel(banco.Model):
    __tablename__ = 'alunos'

    matricula = banco.Column(banco.Integer, primary_key=True)
    nome = banco.Column(banco.String)
    codigos_cursos = banco.relationship('MatriculaModel')
    

    def __init__(self, matricula, nome):
        self.matricula = matricula
        self.nome = nome

    def json(self):
        return{
            'matricula': self.matricula,
            'nome': self.nome,
            'codigos_cursos': [codigos_cursos.json() for codigos_cursos in self.codigos_cursos]
        }
        

    @classmethod
    def find_Aluno(cls, matricula):
        aluno = cls.query.filter_by(matricula=matricula).first()
        if aluno:
            return aluno
        else:
            return None

    def add_Aluno(self):
        banco.session.add(self)
        banco.session.commit()

    def update_Aluno(self, nome):
        self.nome = nome

    def delete_Aluno(self):
        banco.session.delete(self)
        banco.session.commit()
