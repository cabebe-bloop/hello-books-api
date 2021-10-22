# from flask import Blueprint, jsonify

# class Book:
#     def __init__(self, id, title, description):
#         self.id = id
#         self.title = title
#         self.description = description

# book1 = Book(1, "On Earth We're Briefly Gorgeous", "A really moving nonfiction")
# book2 = Book(2, "Name of the WOUND", "Cool fantasy, Rothfuss rules")
# book3 = Book(3, "Dune", "Not sure but everyone tells me it's great")
# books = [book1, book2, book3]

# books_bp = Blueprint("books", __name__, url_prefix="/books")

# @books_bp.route("", methods=["GET"])
# def handle_books():
#     books_response = []
#     for book in books:
#         books_response.append({
#             "id": book.id,
#             "title": book.title,
#             "description": book.description
#         })
#     return jsonify(books_response)

# @books_bp.route("/<book_id>", methods=["GET"])
# def handle_book(book_id):
#     book_id = int(book_id)
#     for book in books:
#         if book.id == book_id:
#             return {
#                 "id": book.id,
#                 "title": book.title,
#                 "description": book.description
#             }