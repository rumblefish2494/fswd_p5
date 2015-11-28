from flask import Flask, url_for, redirect, render_template, request, flash



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
		return render_template('artistList.html')
	return render_template('publicArtistList.html')
#add new artist
@app.route('/artists/new/')
def newArtist():
	login = True
	if login:
		return render_template("newArtist.html")
	return render_template("unauthorized.html")

#edit artist
@app.route('/artists/<int:artist_id>/edit/')
def editArtist(artist_id):
	login = True
	if login:
		return render_template("editArtist.html")
	return render_template("unauthorized.html")

#delete artist
@app.route('/artists/<int:artist_id>/delete/')
def deleteArtist(artist_id):
	login = True
	if login:
		return render_template('deleteArtist.html')
	return render_template('unauthorized.html')

#show list of albums for artist
@app.route('/artists/<int:artist_id>/albums/')
def showAlbums(artist_id):
	login = True
	if login:
		return render_template('albumList.html')
	return render_template('publicAlbumList.html')
#add new album
@app.route('/artists/<int:artist_id>/albums/new/')
def newAlbum(artist_id):
	login = True
	if login:
		return render_template('newAlbum.html')
	return render_template('unauthorized.html')

#edit album
@app.route('/artists/<int:artist_id>/albums/<int:album_id>/edit/')
def editAlbum(artist_id, album_id):
	login = True
	if login:
		return render_template('editAlbum.html')
	return render_template('unauthorized.html')

#delete album
@app.route('/artists/<int:artist_id>/albums/<int:album_id>/delete/')
def deleteAlbum(artist_id, album_id):
	login = True
	if login:
		return render_template('deleteAlbum.html')
	return render_template('unauthorized.html')

#show list of songs for artist/album
@app.route('/artists/<int:artist_id>/albums/<int:album_id>/songs/')
def showSongs(artist_id, album_id):
	login = True
	if login:
		return render_template('songList.html')
	return render_template('publicSongList.html')

#add new song
@app.route('/artists/<int:artist_id>/albums/<int:album_id>/songs/new/')
def newSong(artist_id, album_id):
	login = True
	if login:
		return render_template('newSong.html')
	return render_template('unauthorized.html')


#edit song
@app.route('/artists/<int:artist_id>/albums/<int:album_id>/songs/<int:song_id>/edit/')
def editSongs(artist_id, album_id, song_id):
	login = True
	if login:
		return render_template('editSong.html')
	return render_template('unauthorized.html')

#delete song
@app.route('/artists/<int:artist_id>/albums/<int:album_id>/songs/<int:song_id>/delete/')
def deleteSong(artist_id, album_id, song_id):
	login = True
	if login:
		return render_template('deleteSong.html')
	return render_template('unauthorized.html')




if __name__ == '__main__':
	app.secret_key ='some_secret'
	app.debug = True
	app.run(host = '0.0.0.0', port = 5000)
