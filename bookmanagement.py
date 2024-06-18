# Bookstore managment software

# Bücher hinzufügen funktion.
def book_add(inventory, title, author, price):
    new_book = {
        'title': title,
        'author': author,
        'price': price,
    }
    inventory.append(new_book)

# Bucher auflisten
def book_list(inventory):
    for book in inventory:
            print(f"Titel: {book['title']}, Autor: {book['author']}, Preis: {book['price']}")
                        
# Buch suchen
def book_search(inventor, title):
    for book in inventory:
        if book['title'].lower() == title.lower():
            return book 
    return None

# Buch nach Preis filtern
def book_filter_price(inventory, max_price):
    filtered_books = []
    for book in inventory:
        if book['price'] <= max_price:
            filtered_books.append(book)
    return filtered_books


