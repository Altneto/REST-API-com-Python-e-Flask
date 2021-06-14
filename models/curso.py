from sql_alchemy import banco

class CursoModel(banco.Model):
    __tablename__ = 'cursos'

    codigo = banco.Column(banco.Integer, primary_key=True)
    nome = banco.Column(banco.String)

    def __init__(self, codigo, nome):
        self.codigo = codigo
        self.nome = nome
    
    def json(self):
        return {
            'codigo': self.codigo,
            'nome': self.nome
        }
    
    @classmethod
    def find_curso(cls, codigo):
        curso = cls.query.filter_by(codigo=codigo).first()
        if curso:
            return curso
        return None

    def save_curso(self):
        banco.session.add(self)
        banco.session.commit()

    def update_curso(self, nome):
        self.nome = nome
    
    def delete_curso(self):
        banco.session.delete(self)
        banco.session.commit()