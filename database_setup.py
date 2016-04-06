import sys

from sqlalchemy import Column, ForeignKey, Integer, String

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import relationship

from sqlalchemy import create_engine

Base = declarative_base()

#create users table
class User(Base):
	__tablename__ = 'user'
	name = Column(String, nullable=False)
	id = Column(Integer, primary_key=True)
	email = Column(String)
	picUrl = Column(String)
	#for returning JSON
	@property
	def serialize(self):
		return {
			'name': self.name,
			'id': self.id,
			'email': self.email,
			'picUrl': self.picUrl
		}

#create artists table
class Artist(Base):
	__tablename__ = 'artist'
	name = Column(String, nullable=False)
	id = Column(Integer, primary_key=True)
	bio = Column(String)
	picUrl = Column(String)
	user_id = Column(Integer, ForeignKey("user.id"))
	user = relationship(User)
	#for returning JSON
	@property
	def serialize(self):
		return {
			'name': self.name,
			'id': self.id,
			'bio': self.bio,
			'picUrl': self.picUrl
		}

#create Album table
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
	#for returning JSON
	@property
	def serialize(self):
		return {
			'id': self.id,
			'title': self.title,
			'description': self.description,
			'albumArtUrl': self.albumArtUrl,
			'artist' : self.artist.name
		}
#create Song table
class Song(Base):
	__tablename__ = 'song'
	id = Column(Integer, primary_key=True)
	title = Column(String, nullable=False)
	artist_id = Column(Integer, ForeignKey("artist.id"))
	album_id = Column(Integer, ForeignKey("album.id"))
	user_id = Column(Integer, ForeignKey("user.id"))
	artist = relationship(Artist)
	album = relationship(Album)
	user = relationship(User)
	#for returning JSON
	@property
	def serialize(self):
		return {
			'id': self.id,
			'title': self.title,
			'album': self.album.title,
			'artist': self.artist.name
		}
#create Admin table (for future use)
class Admin(Base):
	__tablename__ = 'admin'
	id = Column(Integer, primary_key=True)
	name = Column(String, nullable=False)
	email = Column(String)
	picUrl = Column(String)

engine = create_engine(
	'postgresql+psycopg2://catalog:Udacity@/catalog')

Base.metadata.create_all(engine)
