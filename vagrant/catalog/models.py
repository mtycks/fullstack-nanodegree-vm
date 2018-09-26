from sqlalchemy import Column,Integer,String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine
from passlib.apps import custom_app_context as pwd_context

Base = declarative_base()


class Category(Base):
    __tablename__ = 'category'

    id = Column(Integer, primary_key=True)
    title = Column(String, index=True)
    description = Column(String)
    user_id = Column(Integer, ForeignKey('user.id'))
    created = Column(DateTime)
    parent = Column(Integer, ForeignKey('category.id'))

    # Serialize function to output JSON for our API
    @property
    def serialize(self):

        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'user_id': self.user_id,
            'created': self.created,
            'parent': self.parent
            }


class Wall(Base):
    __tablename__ = 'wall'

    id = Column(Integer, primary_key=True)
    title = Column(String, index=True)
    description = Column(String)
    user_id = Column(Integer, ForeignKey('user.id'))
    category = Column(Integer, ForeignKey('category.id'))
    created = Column(DateTime)

    # Serialize function to output JSON for our API
    @property
    def serialize(self):

        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'user_id': self.user_id,
            'created': self.created,
            'category': self.category
            }


class WallPhoto(Base):
    __tablename__ = 'wallphoto'

    id = Column(Integer, primary_key=True)
    filename = Column(String, index=True)
    directory = Column(String)
    photo_url = Column(String)
    description = Column(String)
    caption = Column(String)
    wall_id = Column(Integer, ForeignKey('wall.id'))
    user_id = Column(Integer, ForeignKey('user.id'))
    created = Column(DateTime)

    # Serialize function to output JSON for our API
    @property
    def serialize(self):

        return {
            'id': self.id,
            'filename': self.filename,
            'directory': self.directory,
            'photo_url': self.photo_url,
            'description': self.description,
            'caption': self.caption,
            'wall_id': self.wall_id,
            'user_id': self.user_id,
            'created': self.created
            }


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    username = Column(String(32), index=True)
    profile_photo = Column(String)
    cover_photo = Column(String)
    email = Column(String)
    full_name = Column(String)
    password_hash = Column(String(64))
    created = Column(DateTime)

    def hash_password(self, password):
        self.password_hash = pwd_context.encrypt(password)

    def verify_password(self, password):
        return pwd_context.verify(password, self.password_hash)

    # Serialize function to output JSON for our API
    @property
    def serialize(self):

        return {
            'id': self.id,
            'username': self.username,
            'profile_photo': self.profile_photo,
            'cover_photo': self.cover_photo,
            'full_name': self.full_name,
            'email': self.email,
            'created': self.created
            }


engine = create_engine('sqlite:///users.db')


Base.metadata.create_all(engine)
