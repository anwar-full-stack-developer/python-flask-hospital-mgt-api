from app_init import db, mar

class Author(db.Model):
    #  __tablename__ = "author"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))


class AuthorSchema(mar.SQLAlchemySchema):
    class Meta:
        model = Author
        load_instance = True

    id = mar.auto_field()
    name = mar.auto_field()
    # books = mar.auto_field()



class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    author_id = db.Column(db.Integer, db.ForeignKey("author.id"))
    author = db.relationship("Author", backref="books")


class BookSchema(mar.SQLAlchemyAutoSchema):
    author = mar.auto_field()
    class Meta:
        model = Book
        load_instance = True
        fields = ('id', 'title', 'author', 'links')
        include_fk = True


author_schema = AuthorSchema()
authors_schema = AuthorSchema(many=True)

book_schema = BookSchema()
books_schema = BookSchema(many=True)
