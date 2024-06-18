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

# Gesamtwert berechnen
def book_total_value(inventory):
    total = 0
    for book in inventory:
        total += book['price']
    return total


if __name__ == '__main__':
    inventory = []

    book_add(inventory,"Bestes Book", "Unknown", 99.23)
    book_add(inventory,"Get better in python", "python guru", 9.99)
    book_add(inventory, "Advanced git", "the git profi", 12.99)

    print("Print all books")
    book_list(inventory)

    python_book = book_search(inventory, "get better in python")
    print(f"A good book for learning python: {python_book}")

    cheap_books = book_filter_price(inventory, 15)
    print("List all cheap books")
    book_list(cheap_books)

    print(f"Gesamtwert der Bibliothek: {book_total_value(inventory)}")
