from game_app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    score = db.Column(db.Integer)
    def __repr__(self):
        return '<User %r>' % self.name

def init():
    db.create_all()