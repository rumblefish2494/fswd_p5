from sqlalchemy import Column, ForeignKey, Integer, String, create_engine, update
from sqlalchemy.orm import sessionmaker, relationship
from database_setup import Base, Admin, User, Artist, Album, Song
'postgresql:///catalog')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

a1 = Admin(name='Brian',email='rumblefish@sbcglobal.net', picUrl='http://i.telegraph.co.uk/multimedia/archive/02830/cat_2830677b.jpg')
session.add(a1)
session.commit()

u1 = User(name='Brian',email='rumblefish@sbcglobal.net', picUrl='http://i.telegraph.co.uk/multimedia/archive/02830/cat_2830677b.jpg')
session.add(a1)
session.commit()

art1 = Artist(name='Chicago',bio='Chicago is an American rock band formed in 1967 in Chicago,'
	' Illinois. The self-described "rock and roll band with horns" began as a politically charged,'
	' sometimes experimental, rock band and later moved to a predominantly softer sound, generating'
	'several hit ballads. The group had a steady stream of hits throughout the 1970s and 1980s.', picUrl='https://upload.wikimedia.'
	'org/wikipedia/en/a/af/ChicagoAlbum.jpg')
session.add(art1)
session.commit()
