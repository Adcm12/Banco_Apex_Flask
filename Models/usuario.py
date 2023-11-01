from main import db

class Usuario(db.Model):
    
    Nome        = db.Column(db. String(30), primary_key=True)
    Nro_Conta   = db.Column(db. String(10), nullable = False)
    Email       = db.Column(db. String(30), nullable = False)
    Senha       = db.Column(db. String(12), nullable = False)
    Saldo       = db.Column(db. Double, nullable = False)


    def __repr__(self):

        return '<NAME %r' % self.name