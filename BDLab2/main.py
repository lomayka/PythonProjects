from db import Database
import sys
import sqlalchemy

database = Database()

def all_readers(txt):
    readers = database.fetch_all_readers()
    print(readers)


def all_books(txt):
    books = database.fetch_all_books()
    print(books)


def all_authors(txt):
    authors = database.fetch_all_authors()
    print(authors)

def add_book(txt):
    name = txt.split('&')[1]
    annotation = txt.split('&')[2]
    database.insert_book(name, annotation)

def add_reader(txt):
    name = txt.split('&')[1]
    date = txt.split('*')[2]
    database.insert_reader(name, date)


def add_author(txt):
    name = txt.split('&')[1]
    date = txt.split('*')[1]
    bookid = txt.split('*')[1]
    database.insert_author(name, date, bookid)


def reader_by_name(txt):
    name = txt.split('&')[1]
    reader = database.reader_by_name(name)
    print(reader[2], reader[0], reader[1])


def author_by_name(txt):
    name = txt.split('&')[1]
    authors = database.find_authors_by_part_name(name)
    for author in authors:
        print(author[2], author[0], author[1])


def authors_by_date(txt):
    start_date = txt.split('&')[1]
    end_date = txt.split('&')[2]
    results = database.search_authors_by_date(start_date, end_date)
    print(results)


def reader_by_book_annotation(txt):
    phrase = txt.split('&')[1]
    results = database.find_readers_by_annotation(phrase)
    print(txt.split('&')[1])
    for result in results:
        print(result[2], result[0], " Annotation:", result[1])


def remove_reader(txt):
    id = txt.split(' ')[1]
    database.delete_reader(id)


def remove_author(txt):
    id = txt.split(' ')[1]
    database.delete_author(id)


def remove_book(txt):
    id = txt.split(' ')[1]
    database.delete_book(id)


def close_programm(txt):
    sys.exit()

commands = {
    'allReaders': all_readers,
    'allBooks': all_books,
    'allAuthors': all_authors,
    'addReader': add_reader,
    'addBook': add_book,
    'addAuthor': add_author,
    'removeReader': remove_reader,
    'removeAuthor': remove_author,
    'removeBook': remove_book,
    'readerByName': reader_by_name,
    'readerByAnnotation': reader_by_book_annotation,
    'authorsByDate': authors_by_date,
    'authorByName': author_by_name,
    'close': close_programm
}

while 1:
    text = input("Enter Command:")
    command = text.split(' ')[0]

    if command in commands:
        commands[command](text)

