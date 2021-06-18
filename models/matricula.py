from sql_alchemy import banco

class MatriculaModel(banco.Model):
    __tablename__ = 'matriculas'

    id_matricula = banco.Column(banco.Integer, primary_key=True)
    matricula = banco.Column(banco.Integer, banco.ForeignKey('alunos.matricula'))
    codigo_curso = banco.Column(banco.Integer, banco.ForeignKey('cursos.codigo'))
    frequencia = banco.Column(banco.String)
    media = banco.Column(banco.Float)


    def __init__(self, matricula, codigo_curso, frequencia, media):
        self.matricula = matricula
        self.codigo_curso = codigo_curso
        self.frequencia = frequencia
        self.media = media
    
    def json(self):
        return {
            'matricula': self.matricula,
            'codigo_curso': self.codigo_curso,
            'frequencia': self.frequencia,
            'media': self.media
        }
    
    @classmethod
    def find_matricula(cls, matricula):
        matricula = cls.query.filter_by(matricula=matricula).first()
        if matricula:
            return matricula
        return None

    @classmethod
    def find_codigo(cls, codigo_curso):
        codigo_curso = cls.query.filter_by(codigo_curso=codigo_curso).first()
        if codigo_curso:
            return codigo_curso
        return None

    def save_matricula(self):
        banco.session.add(self)
        banco.session.commit()

    def update_matricula(self, codigo_curso, frequencia, media):
        self.codigo_curso = codigo_curso
        self.frequencia = frequencia
        self.media = media 
    
    def delete_matricula(self, matricula):
        banco.session.delete(matricula)
        banco.session.commit()