from flask import Blueprint, render_template, request, redirect, url_for
from app.services import get_books, add_book, delete_book, update_book, get_book

bp = Blueprint('main', __name__)

# Page principale
@bp.route('/')
@bp.route('/books')
def index():
    status_filter = request.args.get('status')
    books = get_books(status_filter)
    return render_template('index.html', books=books)

# Ajouter un livre
@bp.route('/books', methods=['POST'])
def add():
    title = request.form['title']
    author = request.form['author']
    status = request.form['status']
    add_book(title, author, status)
    return redirect(url_for('main.index'))

# Supprimer un livre
@bp.route('/delete/<int:book_id>')
def delete(book_id):
    delete_book(book_id)
    return redirect(url_for('main.index'))

# Éditer un livre
@bp.route('/edit/<int:book_id>')
def edit(book_id):
    book = get_book(book_id)
    if book:
        return render_template('index.html', edit_book=book, books=get_books())
    return "Livre non trouvé", 404

# Sauvegarder les modifications
@bp.route('/update/<int:book_id>', methods=['POST'])
def update(book_id):
    title = request.form['title']
    author = request.form['author']
    status = request.form['status']
    update_book(book_id, title, author, status)
    return redirect(url_for('main.index'))
