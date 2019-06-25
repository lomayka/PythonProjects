import random

import pandas as pd

from schemes import BookScheme
from schemes import AuthorScheme
from schemes import ReadersScheme

from schemes import Base

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime


class Database:

    _engine_ = create_engine('postgresql://postgres:123@localhost/library')
    _Session_ = sessionmaker(bind=_engine_)

    def __init__(self):
        _engine_ = create_engine('postgresql://postgres:123@localhost/library')
        _Session_ = sessionmaker(bind=_engine_)
        Base.metadata.create_all(_engine_)
        self._session_ = _Session_()

    def close(self):
        self._session_.close()

    def get_book(self, book_id):
        res = self._session_.query(BookScheme).get(book_id)
        return str(res.name) + "    " + res.annotation

    def fetch_all_books(self):
        res = self._session_.query(BookScheme).all()
        strings = ""
        for i in res:
            strings += str(i.id) + "   " + i.name + "    " + str(i.annotation) + "\n"
        return strings

    def insert_book(self, book_scheme: BookScheme):
        self._session_.add(book_scheme)
        self._session_.commit()

    def update_book(self, book_scheme: BookScheme):
        self.insert_book(book_scheme)

    def delete_book(self, book_id):
        book = self._session_.query(BookScheme).get(book_id)
        self._session_.delete(book)
        self._session_.commit()

    def get_reader(self, reader_id):
        res = self._session_.query(ReadersScheme).get(reader_id)
        return res.name + " " + res.registrationdate

    def fetch_all_readers(self):
        res = self._session_.query(ReadersScheme).all()
        strings = ""
        for i in res:
            strings += str(i.id) + "   " + i.name + "    " + str(i.registrationdate) + "\n"
        return strings

    def insert_reader(self, reader_scheme: ReadersScheme):
        self._session_.add(reader_scheme)
        self._session_.commit()

    def update_reader(self, reader_scheme: ReadersScheme):
        self.insert_reader(reader_scheme)

    def delete_reader(self, reader_id):
        reader = self._session_.query(ReadersScheme).get(reader_id)
        self._session_.delete(reader)
        self._session_.commit()

    def get_author(self, author_id):
        res = self._session_.query(AuthorScheme).get(author_id)
        return res.name + " " + res.birthdate

    def fetch_all_authors(self):
        res = self._session_.query(AuthorScheme).all()
        strings = ""
        for i in res:
            strings += str(i.id) + "   " + i.name + "    " + str(i.birthdate) + "\n"
        return strings

    def insert_author(self, author_scheme: AuthorScheme):
        self._session_.add(author_scheme)
        self._session_.commit()

    def update_author(self, author_scheme: AuthorScheme):
        self.insert_author(author_scheme)

    def delete_author(self, author_id):
        author = self._session_.query(AuthorScheme).get(author_id)
        self._session_.delete(author)
        self._session_.commit()

    def search_authors_by_date(self, left_boundary, right_boundary):
        res = self._session_.query(AuthorScheme, ) \
            .filter(AuthorScheme.birthdate >= left_boundary,
                    AuthorScheme.birthdate < right_boundary) \
            .all()
        strings = ""
        for row in res:
            strings += str(row.id) + "  " + row.name + "    " + str(row.birthdate) + "\n"
        return strings

    def search_books_by_annotation(self, annotation):
        sql = """SELECT * FROM books to_tsvector(books.annotation) @@ phraseto_tsquery('%s')""" %annotation
        res = self._session_.execute(sql).fetchall()

        strings = ""
        for row in res:
            strings += str(row.id) + "  " + row.name + "    " + row.annotation
