from flask import Flask, url_for, redirect, render_template, request, flash, jsonify
from sqlalchemy import Column, ForeignKey, Integer, String, create_engine, update
from sqlalchemy.orm import sessionmaker, relationship
from database_setup import Base, Admin, User, Artist, Album, Song

engine = create_engine('sqlite:///echochamber.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


app = Flask(__name__)



#login page
@app.route('/login/')
def login():

	return render_template('login.html')

#show list of artists
@app.route('/artists/')
def showArtists():
	login = True
	if login:
		artists = session.query(Artist).all()
		return render_template('artistList.html', artists=artists)
	return render_template('publicArtistList.html')
#add new artist
@app.route('/artists/new/', methods=['GET', 'POST'])
def newArtist():
	if request.method == 'POST':
		newArtist = Artist(name=request.form['name'], bio=request.form['bio'], picUrl=request.form['picture'])
		session.add(newArtist)
		session.commit()
		flash("New artist has been added!")
		return redirect(url_for('showArtists'))
	login = True
	if login:
		return render_template("newArtist.html")
	return render_template("unauthorized.html")

#edit artist
@app.route('/artists/<int:artist_id>/edit/', methods=['GET', 'POST'])
def editArtist(artist_id):
	login = True
	if login:
		artist = session.query(Artist).filter_by(id=artist_id).one()
		bio = artist.bio
		print artist.bio
		if request.method == 'POST':
			artist.name = request.form['name']
			artist.picUrl = request.form['picture']
			artist.bio = request.form['bio']
			session.add(artist)
			session.commit()
			flash(artist.name + " has been edited!")
			return redirect(url_for('showAlbums', artist_id=artist_id))
		return render_template("editArtist.html", artist=artist, bio=bio)
	return render_template("unauthorized.html")

#delete artist
@app.route('/artists/<int:artist_id>/delete/', methods=['GET','POST'])
def deleteArtist(artist_id):
	login = True
	if login:
		artist = session.query(Artist).filter_by(id=artist_id).one()
		songs = session.query(Song).filter_by(artist_id=artist_id).all()
		if request.method == 'POST':
			print len(songs)
			for s in songs:
				print s.title

			print artist.name
			if len(songs) == 0:
				session.delete(artist)
				session.commit()
				flash("Artist succesfully deleted.")
				return redirect(url_for('showArtists'))
			flash("You cannot delete artists that have existing songs.")
			return render_template('unauthorized.html')
		return render_template('deleteArtist.html', artist=artist)
	return render_template('unauthorized.html')

#show list of albums for artist
@app.route('/artists/<int:artist_id>/albums/')
def showAlbums(artist_id):
	login = True
	if login:
		artist = session.query(Artist).filter_by(id=artist_id).one()
		albums = session.query(Album).filter_by(artist_id=artist_id).all()
		print artist_id
		for a in albums:
			print a.artist_id
			print a.title
			print a.description
		return render_template('albumList.html', albums=albums, artist=artist)
	return render_template('publicAlbumList.html')
#add new album
@app.route('/artists/<int:artist_id>/albums/new/', methods=['GET', 'POST'])
def newAlbum(artist_id):
	login = True
	if login:
		artist = session.query(Artist).filter_by(id=artist_id).one()
		albums = session.query(Album).filter_by(id=artist_id).all()
		print artist_id

		if request.method == 'POST':
			nAlbum = Album(title=request.form['title'], description=request.form['info'], albumArtUrl=request.form['picture'], artist_id=artist.id, user_id=1)
			session.add(nAlbum)
			session.commit()
			flash("Album " + nAlbum.title + " has been added to " + artist.name)
			return redirect(url_for('showAlbums', artist_id=artist_id))
		return render_template('newAlbum.html', albums=albums, artist=artist)
	return render_template('unauthorized.html')

#edit album
@app.route('/artists/<int:artist_id>/albums/<int:album_id>/edit/', methods=['GET', 'POST'])
def editAlbum(artist_id, album_id):
	login = True
	if login:
		artist = session.query(Artist).filter_by(id=artist_id).one()
		album = session.query(Album).filter_by(id=album_id).one()
		if request.method == 'POST':
			album.title = request.form['title']
			album.albumArtUrl = request.form['picture']
			album.description = request.form['description']
			session.add(album)
			session.commit()
			flash("Album " + album.title + " has been edited.")
			return redirect(url_for('showSongs', artist_id=artist_id, album_id=album_id))
		return render_template('editAlbum.html', artist=artist, album=album)
	return render_template('unauthorized.html')

#delete album
@app.route('/artists/<int:artist_id>/albums/<int:album_id>/delete/', methods=['GET', 'POST'])
def deleteAlbum(artist_id, album_id):
	login = True
	if login:
		artist = session.query(Artist).filter_by(id=artist_id).one()
		album = session.query(Album).filter_by(id=album_id).one()
		songs = session.query(Song).filter_by(album_id=album_id).all()
		print len(songs)
		if request.method == 'POST':
			if len(songs) == 0:
				session.delete(album)
				session.commit()
				flash("Album has been deleted.")
				return redirect(url_for('showAlbums', artist_id=artist_id))
			flash("You must delete all songs first.")
			return render_template('unauthorized.html')
		return render_template('deleteAlbum.html', artist=artist, album=album)
	return render_template('unauthorized.html')

#show list of songs for artist/album
@app.route('/artists/<int:artist_id>/albums/<int:album_id>/songs/')
def showSongs(artist_id, album_id):
	login = True
	if login:
		artist = session.query(Artist).filter_by(id=artist_id).one()
		album = session.query(Album).filter_by(id=album_id).one()
		songs = session.query(Song).filter_by(album_id=album_id).all()
		return render_template('songList.html', artist=artist, album=album, songs=songs)
	return render_template('publicSongList.html')

#add new song
@app.route('/artists/<int:artist_id>/albums/<int:album_id>/songs/new/', methods=['GET', 'POST'])
def newSong(artist_id, album_id):
	login = True
	if login:
		artist = session.query(Artist).filter_by(id=artist_id).one()
		album = session.query(Album).filter_by(id=album_id).one()
		if request.method == 'POST':
			nSong = Song(title=request.form['name'], album_id=album_id, artist_id=artist_id, user_id=1)
			session.add(nSong)
			session.commit()
			flash("Song " + nSong.title + " has been added")
			return redirect(url_for('showSongs', artist_id=artist_id, album_id=album_id))
		return render_template('newSong.html', artist= artist, album=album)
	return render_template('unauthorized.html')


#edit song
@app.route('/artists/<int:artist_id>/albums/<int:album_id>/songs/<int:song_id>/edit/', methods=['GET', 'POST'])
def editSong(artist_id, album_id, song_id):
	login = True
	if login:
		artist = session.query(Artist).filter_by(id=artist_id).one()
		album = session.query(Album).filter_by(id=album_id).one()
		song = session.query(Song).filter_by(id=song_id).one()
		if request.method == 'POST':
			song.title = request.form['title']
			session.add(song)
			session.commit()
			flash(song.title + " has been edited.")
			return redirect(url_for('showSongs', artist_id=artist_id, album_id=album_id))
		return render_template('editSong.html', artist=artist, album=album, song=song)
	return render_template('unauthorized.html')

#delete song
@app.route('/artists/<int:artist_id>/albums/<int:album_id>/songs/<int:song_id>/delete/', methods=['GET', 'POST'])
def deleteSong(artist_id, album_id, song_id):
	login = True
	if login:
		artist = session.query(Artist).filter_by(id=artist_id).one()
		album = session.query(Album).filter_by(id=album_id).one()
		song = session.query(Song).filter_by(id=song_id).one()
		if request.method == 'POST':
			if song.user_id == 1:
				session.delete(song)
				session.commit()
				flash("Song has been deleted from " + album.title)
				return redirect(url_for('showSongs', artist_id=artist_id, album_id=album_id))
			return render_template('unauthorized.html')
		return render_template('deleteSong.html', artist_id=artist_id, album_id=album_id, song=song)
	return render_template('unauthorized.html')

#API endpoint to return artists
@app.route('/artists/JSON/')
def returnArtists():
	artists = session.query(Artist).all()
	return jsonify(Artists=[a.serialize for a in artists])

@app.route('/artists/<int:artist_id>/JSON/')
def returnArtist(artist_id):
	artist = session.query(Artist).filter_by(id=artist_id).one()
	return jsonify(artist.serialize)

#API endpoint to return albums
@app.route('/albums/JSON/')
def returnAlbums():
	albums = session.query(Album).all()
	return jsonify(Albums=[a.serialize for a in albums])

@app.route('/albums/<int:album_id>/JSON/')
def returnAlbum(album_id):
	album = session.query(Album).filter_by(id=album_id).one()
	return jsonify(album.serialize)

@app.route('/songs/JSON/')
def returnSongs():
	songs = session.query(Song).all()
	return jsonify(Songs=[s.serialize for s in songs])

@app.route('/songs/<int:song_id>/JSON/')
def returnSong(song_id):
	song = session.query(Song).filter_by(id=song_id).one()
	return jsonify(song.serialize)

if __name__ == '__main__':
	app.secret_key ='some_secret'
	app.debug = True
	app.run(host = '0.0.0.0', port = 5000)
