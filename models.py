from app import db

# Tables for database
class Comic(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    publisher = db.Column(db.String(32))
    author = db.Column(db.String(32), nullable=False)
    artist = db.Column(db.String(32), nullable=False)
    publication_date = db.Column(db.Date())
    completed = db.Column(db.String(32))

    def __repr__(self):
        return f'<Comic {self.title}>'
