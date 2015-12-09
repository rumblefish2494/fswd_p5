import sys

from sqlalchemy import Column, ForeignKey, Integer, String

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import relationship

from sqlalchemy import create_engine

Base = declarative_base()

class User(Base):
	__tablename__ = 'user'
	name = Column(String, nullable=False)
	id = Column(Integer, primary_key=True)
	email = Column(String)
	picUrl = Column(String)

class Artist(Base):
	__tablename__ = 'artist'
	name = Column(String, nullable=False)
	id = Column(Integer, primary_key=True)
	bio = Column(String)
	picUrl = Column(String)
	user_id = Column(Integer, ForeignKey("user.id"))
	user = relationship(User)

	@property
	def serialize(self):
		return {
			'id': self.id,
			'name': self.name,
			'bio': self.bio,
			'picUrl': self.picUrl
		}


class Album(Base):
	__tablename__ = 'album'
	title = Column(String, nullable=False)
	id = Column(Integer, primary_key=True)
	albumArtUrl = Column(String)
	description = Column(String)
	artist_id = Column(Integer, ForeignKey("artist.id"))
	artist = relationship(Artist)
	user_id = Column(Integer, ForeignKey("user.id"))
	user = relationship(User)

class Song(Base):
	__tablename__ = 'song'
	id = Column(Integer, primary_key=True)
	title = Column(String, nullable=False)
	artist_id = Column(Integer, ForeignKey("artist_id"))
	album_id = Column(Integer, ForeignKey("album.id"))
	user_id = Column(Integer, ForeignKey("user.id"))
	artist_id = relationship(Artist)
	album = relationship(Album)
	user = relationship(User)


class Admin(Base):
	__tablename__ = 'admin'
	id = Column(Integer, primary_key=True)
	name = Column(String, nullable=False)
	email = Column(String)
	picUrl = Column(String)

engine = create_engine(
	'sqlite:///echochamber.db')

Base.metadata.create_all(engine)