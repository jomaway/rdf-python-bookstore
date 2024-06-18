# Bookstore managment software

# Bücher hinzufügen funktion.
def book_add(inventory, title, author, price):
    new_book = {
        'title': title,
        'author': author,
        'preis': price,
    }
    inventory.append(new_book)


