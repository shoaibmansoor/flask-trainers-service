from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Trainer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    specialization = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f'<Trainer {self.name}>'
