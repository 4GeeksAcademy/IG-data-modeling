import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Users(Base):
    __tablename__ = 'users'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False)
    firstname = Column(String(50), nullable=False)
    lastname = Column(String(50), nullable=False)
    email = Column(String(250), nullable=False, unique=True)


class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    title = Column(String(250), nullable=False)
    description = Column(String(500))
    body = Column(String(2500), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))
    users = relationship(Users)

    def to_dict(self):
        return {}



class Followers(Base):
    __tablename__ = 'followers'
    id = Column(Integer, primary_key=True)
    user_from_id = Column(Integer, ForeignKey('users.id'))
    user_to_id = Column(Integer, ForeignKey("users.id"))
    user_to = relationship("Users", foreign_keys=["user_from_id"])
    user_from= relationship("Users", foreign_keys=["user_to_id"])


class Media(Base):
    __tablename__ = 'media'
    id = Column(Integer, primary_key=True)
    #type = Column(Enum(MediaType))
    url = Column(String, nullable=True)
    post_id = Column(Integer, ForeignKey('post.id'))
    post = relationship(Post)


class Comments(Base):
    __tablename__ = 'comments'
    id = Column(Integer, primary_key=True)
    comment_text = Column(String(2500), nullable=False)
    author_id = Column(Integer, ForeignKey('users.id'))
    author = relationship('Users', foreign_keys=['author_id'])
    post_id = Column(Integer, ForeignKey('post.id'))
    post = relationship('Post', foreign_keys=['post_id'])


## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
