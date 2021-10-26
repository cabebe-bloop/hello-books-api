from app import db
from app.models.book import Book
from flask import Blueprint, jsonify, make_response, request

books_bp = Blueprint("books", __name__, url_prefix="/books")

@books_bp.route("", methods=["GET", "POST"])
def handle_books():
    if request.method == "POST":
        request_body = request.get_json()
        new_book = Book(title = request_body["title"], 
                        description = request_body["description"])
        db.session.add(new_book)
        db.session.commit()

        return make_response(f"Book {new_book.title} successfully created", 201)
    elif request.method == "GET":
        books = Book.query.all()
        books_response = []
        for book in books:
            books_response.append({
                "id": book.id,
                "title": book.title,
                "description": book.description
            })
        return jsonify(books_response)

@books_bp.route("/<book_id>", methods=["GET", "PUT", "DELETE"])
def handle_book(book_id):
    book = Book.query.get(book_id)
    if book is None:
            return make_response("", 404)

    if request.method == "GET":
        return {
            "id": book.id,
            "title": book.title,
            "description": book.description
        }
    elif request.method == "PUT":
        request_body = request.get_json()
        book.title = request_body["title"]
        book.description = request_body["description"]

        db.session.commit()

        return make_response(f"Book #{book.id} successfully updated")
    elif request.method == "DELETE":
        db.session.delete(book)
        db.session.commit()
        return make_response(f"Book #{book.id} successfully deleted")

@books_bp.route("/limit/<amount>", methods=["GET"])
def handle_limit(amount):
    books = Book.query.limit(amount).all()
    if books is None:
        return make_response("", 404)
    books_response = []
    for book in books:
        books_response.append({
            "id": book.id,
            "title": book.title,
            "description": book.description
        })
    return jsonify(books_response)