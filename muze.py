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

@app.route('/artists/<int:artist_id>/edit/')
def editArtist(artist_id):
	output = ""
	output += '<h1>'
	output += 'EDIT ARTIST'
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

#show list of songs for artist/album
@app.route('/artists/<int:artist_id>/albums/<int:album_id>/songs/')
def showSongs(artist_id, album_id):
	output = ""
	output += '<h1>'
	output += 'SONG LIST'
	output += '</h1>'
	return output




if __name__ == '__main__':
	app.secret_key ='some_secret'
	app.debug = True
	app.run(host = '0.0.0.0', port = 5000)
