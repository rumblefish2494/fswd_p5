from flask import Flask, url_for, redirect, render_template, request, flash



app = Flask(__name__)

#login page
@app.route('/login/')
def login():
	output = ""
	output += '<h1>'
	output += 'LOGIN'
	output += '</h1>'
	return output

#show list of artists
@app.route('/artists/')
def showArtists():
	output = ""
	output += '<h1>'
	output += 'ARTIST LIST'
	output += '</h1>'
	return output

#add new artist
@app.route('/artists/new/')
def newArtist():
	output = ""
	output += '<h1>'
	output += 'ADD ARTIST'
	output += '</h1>'
	return output

#edit artist
@app.route('/artists/<int:artist_id>/edit/')
def editArtist(artist_id):
	output = ""
	output += '<h1>'
	output += 'EDIT ARTIST'
	output += '</h1>'
	return output

#delete artist
@app.route('/artists/<int:artist_id>/delete/')
def deleteArtist(artist_id):
	output = ""
	output += '<h1>'
	output += 'DELETE ARTIST'
	output += '</h1>'
	return output

#show list of albums for artist
@app.route('/artists/<int:artist_id>/albums/')
def showAlbums(artist_id):
	output = ""
	output += '<h1>'
	output += 'ALBUM LIST'
	output += '</h1>'
	return output

#add new album
@app.route('/artists/<int:artist_id>/albums/new/')
def newAlbum(artist_id):
	output = ""
	output += '<h1>'
	output += 'ADD ALBUM'
	output += '</h1>'
	return output

#edit album
@app.route('/artists/<int:artist_id>/albums/<int:album_id>/edit/')
def editAlbum(artist_id, album_id):
	output = ""
	output += '<h1>'
	output += 'EDIT ALBUM'
	output += '</h1>'
	return output

#delete album
@app.route('/artists/<int:artist_id>/albums/<int:album_id>/delete/')
def deleteAlbum(artist_id, album_id):
	output = ""
	output += '<h1>'
	output += 'DELETE ALBUM'
	output += '</h1>'
	return output

#show list of songs for artist/album
@app.route('/artists/<int:artist_id>/albums/<int:album_id>/songs/')
def showSongs(artist_id, album_id):
	output = ""
	output += '<h1>'
	output += 'SONG LIST'
	output += '</h1>'
	return output

#add new song
@app.route('/artists/<int:artist_id>/albums/<int:album_id>/songs/new/')
def newSong(artist_id, album_id):
	output = ""
	output += '<h1>'
	output += 'ADD SONG'
	output += '</h1>'
	return output

#edit song
@app.route('/artists/<int:artist_id>/albums/<int:album_id>/songs/<int:song_id>/edit/')
def editSongs(artist_id, album_id, song_id):
	output = ""
	output += '<h1>'
	output += 'EDIT SONG'
	output += '</h1>'
	return output

#delete song
@app.route('/artists/<int:artist_id>/albums/<int:album_id>/songs/<int:song_id>/delete/')
def deleteSong(artist_id, album_id, song_id):
	output = ""
	output += '<h1>'
	output += 'DELETE SONG'
	output += '</h1>'
	return output




if __name__ == '__main__':
	app.secret_key ='some_secret'
	app.debug = True
	app.run(host = '0.0.0.0', port = 5000)
