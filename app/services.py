from app.models import books

# Récupérer tous les livres, éventuellement avec un filtre de statut
def get_books(status=None):
    if status:
        return [b for b in books if b['status'] == status]
    return books

# Ajouter un livre
def add_book(title, author, status):
    books.append({
        'id': len(books),
        'title': title,
        'author': author,
        'status': status
    })

# Supprimer un livre par ID
def delete_book(book_id):
    global books
    books[:] = [b for b in books if b['id'] != book_id]
    # Réattribuer les IDs
    for idx, book in enumerate(books):
        book['id'] = idx

# Récupérer un livre par ID
def get_book(book_id):
    return next((b for b in books if b['id'] == book_id), None)

# Modifier un livre
def update_book(book_id, title, author, status):
    for book in books:
        if book['id'] == book_id:
            book['title'] = title
            book['author'] = author
            book['status'] = status
            break
