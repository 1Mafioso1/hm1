class Book:
    def __init__(self, title, authors, year) -> None:
        self.title = title
        self.authors = authors
        self.year = year

    def __str__(self) -> str:
        return f'Назва: {self.title}\nАвтори: {", ".join(self.authors)}\nРік: {self.year}'


class Library:
    def __init__(self, name, address) -> None:
        self.name = name
        self.address = address
        self.books = []

    def __str__(self) -> str:
        return f'Бібліотека: {self.name}\nАдреса: {self.address}\nКількість книг: {len(self.books)}'

    def show_books(self):
        if len(self.books) == 0:
            print('У бібліотеці немає книг.')
        else:
            print('\n=== Список книг ===')
            for book in self.books:
                print(book)
                print('----------------')

    def add_book(self, book):
        self.books.append(book)
        print(f'Книгу "{book.title}" додано.')

    def remove_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                self.books.remove(book)
                print(f'Книгу "{title}" видалено.')
                return
        print('Книгу не знайдено.')

    def find_by_title(self, title):
        found = False

        for book in self.books:
            if title.lower() in book.title.lower():
                print(book)
                print('----------------')
                found = True

        if not found:
            print('Книгу не знайдено.')

    def find_by_author(self, author):
        found = False

        for book in self.books:
            for a in book.authors:
                if author.lower() in a.lower():
                    print(book)
                    print('----------------')
                    found = True

        if not found:
            print('Автора не знайдено.')

library = Library('Центральна бібліотека', 'вул. Шевченка 10')

book1 = Book('Кобзар', ['Тарас Шевченко'], 1840)
book2 = Book('Майстер і Маргарита', ['Михайло Булгаков'], 1967)
book3 = Book('Гаррі Поттер', ['Джоан Роулінг'], 1997)

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

print('\n=== Інформація про бібліотеку ===')
print(library)

library.show_books()

print('\n=== Пошук за назвою ===')
library.find_by_title('гаррі')

print('\n=== Пошук за автором ===')
library.find_by_author('Шевченко')

print('\n=== Видалення книги ===')
library.remove_book('Кобзар')

library.show_books()