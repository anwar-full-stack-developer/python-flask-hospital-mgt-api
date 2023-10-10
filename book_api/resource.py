from flask import request, make_response, abort
from flask_restful import Resource
from app_init import db
from .models import Author, AuthorSchema, author_schema, authors_schema
from .models import Book, book_schema, books_schema


class AuthorList(Resource):
    def get(self):
        # Get all the Author from the database.
        authors = Author.query.all()
        return authors_schema.dump(authors)
    
    def post(self):
        # Get the JSON data from the request.
        data = request.get_json()
        # Check if the data is valid.
        if not data:
            return {'message': 'No input data provided'}, 400
        if not data['name']:
            return {'message': 'Name is required'}, 400
        name = data['name']
        # Data validation
  
        existing = Author.query.filter(Author.name == name).one_or_none()
        if existing is None:
            new_author = author_schema.load(request.get_json())
            db.session.add(new_author)
            db.session.commit()
            return author_schema.dump(new_author), 201
        else:
            abort(406, f"Author with name {name} already exists")


class AuthorDetail(Resource):
    def get(self, id):
        # author = Author.query.get(id)
        author = Author.query.filter(Author.id == id).one_or_none()

        if author is not None:
            return author_schema.dump(author)
        else:
            abort(404, f"Author with id {id} not found")

    def put(self, id):
        existing = Author.query.filter(Author.id == id).one_or_none()

        if existing:
            update_person = author_schema.load(request.get_json())
            existing.name = update_person.name
            db.session.merge(existing)
            db.session.commit()
            return author_schema.dump(existing), 201
        else:
            abort(404, f"Author with id {id} not found")

    def delete(self, id):
        author = Author.query.filter(Author.id == id).one_or_none()
        if author:
            db.session.delete(author)
            db.session.commit()
            return make_response(f"{id} successfully deleted", 200)
        else:
            abort(404, f"Author with id {id} not found")


class BookList(Resource):
    def get(self):
        books = Book.query.all()
        return books_schema.dump(books)
    
    def post(self):
        print(request.get_json())
        data = request.get_json()
        # author = Author.query.get(data['author'])
        # print(author)

        # data['author'] = author
        book = book_schema.load(data)
        db.session.add(book)
        db.session.commit()
        return book_schema.dump(book), 201
    

class BookDetail(Resource):
    def get(self, id):
        book = Book.query.filter(Book.id == id).one_or_none()
        if book is not None:
            return book_schema.dump(book)
        else:
            abort(404, f"Book with id {id} not found")

    def put(self, id):
        book = Book.query.filter(Book.id == id).one_or_none()
        
        if book:
            update_book = book_schema.load(request.get_json())
            book.title = update_book.title
            book.author = update_book.author
            db.session.merge(book)
            db.session.commit()
            return book_schema.dump(book), 201
        else:
            abort(404, f"Book with id {id} not found")

    def delete(self, id):
        book = Book.query.filter(Book.id == id).one_or_none()
        if book:
            db.session.delete(book)
            db.session.commit()
            return make_response(f"{id} successfully deleted", 200)
        else:
            abort(404, f"Book with id {id} not found")