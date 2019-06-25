from sqlalchemy import Column, String, Integer, Date, Table, ForeignKey
import random_generator
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


book_reader = Table('taken', Base.metadata,
                Column('readerid', Integer, ForeignKey('reader.id')),
                Column('bookid', Integer, ForeignKey('book.id')))


written = Table('written', Base.metadata,
                Column('authorid', Integer, ForeignKey('authors.id')),
                Column('bookid', Integer, ForeignKey('books.id')))


class BookScheme(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    annotation = Column(String)
    authors = relationship("AuthorScheme",
                           secondary=written,
                           back_populates="books")

    def __init__(self,
                 BookName="",
                 Annotation=""):
        self.name = BookName
        self.annotation = Annotation


class AuthorScheme(Base):
    __tablename__ = "authors"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    birthdate = Column(Date)
    books = relationship("BookScheme",
                         secondary=written,
                         back_populates="authors")

    def __init__(self,
                 name="",
                 birthdate=random_generator.random_date("1750-01-01", "2018-01-01")):
        self.name = name
        self.birthdate = birthdate


class ReadersScheme(Base):
    __tablename__ = "readers"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    registrationdate = Column(Date)

    def __init__(self,
                 name="",
                 date=random_generator.random_date("1980-01-01", "2018-01-01")):
        self.name = name
        self.registrationdate = date