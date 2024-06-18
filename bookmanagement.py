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
           
           
