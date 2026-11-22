import os
os.environ["DISABLE_SQLALCHEMY_CEXT"] = "1"

from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'
db = SQLAlchemy(app)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_name = db.Column(db.String(100), unique=True, nullable=False)
    author = db.Column(db.String(80), nullable=False)
    publisher = db.Column(db.String(80), nullable=False)

    def __repr__(self):
        return f"{self.book_name} by {self.author} ({self.publisher})"


@app.route('/')
def index():
    return 'Books API is running!'

@app.route('/books')
def get_books():
    books = Book.query.all()

    output = []
    for book in books:
        book_data = {
            'id': book.id,
            'book_name': book.book_name,
            'author': book.author,
            'publisher': book.publisher
        }
        output.append(book_data)

    return {"books": output}

@app.route('/books/<int:id>')
def get_book(id):
    book = Book.query.get_or_404(id)
    return {
        "id": book.id,
        "book_name": book.book_name,
        "author": book.author,
        "publisher": book.publisher
    }

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)