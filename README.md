UDACITY FSWD
PROJECT 5 - LINUX SERVER CONFIG -
BRIAN HARLIN
4/10/16

+++++++++++++SERVER INSTRUCTIONS:


==============================================================
LOCATIONS:
==============================================================
GITHUB REPO: https://github.com/rumblefish2494/fswd_p5

AMAZON AWS -
IP ADDRESS: 52.36.139.219
SSH PORT: 2200
URL OF WEB APP: ec2-52-36-139-219.us-west-2.compute.amazonaws.com

==============================================================
INSTALLED SOFTWARE:
==============================================================
oath2client
psqlalchemy
psycopg2
requests
Flasky
httplib2
flask-seasurf
fail2ban
python
python-httplib2
postgresql
apache2

==============================================================
RESOURCES:
==============================================================
-Project 5 Resources - Udacity FSND P5 forum
https://discussions.udacity.com/t/project-5-resources/28343

-Markedly underwhelming and potentially wrong resource list for P5 - Udacity FSND P5 forum
https://discussions.udacity.com/t/markedly-underwhelming-and-potentially-wrong-resource-list-for-p5/8587

-P5 How I got through it - Udacity FSND P5 forum
https://discussions.udacity.com/t/p5-how-i-got-through-it/15342

-A Step by Step Guide to Install LAMP (Linux, Apache, MySQL, Python) on Ubuntu - Udactiy blog
http://blog.udacity.com/2015/03/step-by-step-guide-install-lamp-linux-apache-mysql-python-ubuntu.html

-FSND-P5_Linux-Server-Configuration walthrough - Udacity FSND P5 forum (in comments of P5 How I got through it)
https://github.com/stueken/FSND-P5_Linux-Server-Configuration

-postgres auth
http://stackoverflow.com/questions/18664074/getting-error-peer-authentication-failed-for-user-postgres-when-trying-to-ge

-Postgres - sqlAlcheym; connecting with psycopg2
http://docs.sqlalchemy.org/en/latest/dialects/postgresql.html#dialect-postgresql-psycopg2-connect

-Postgres Engine with sqlAlchemy:
http://docs.sqlalchemy.org/en/latest/core/engines.html

-Postgres configuring pg_hba.conf file
http://www.postgresql.org/docs/9.1/static/auth-pg-hba-conf.html

-Python sudo - ask Ubuntu
http://askubuntu.com/questions/168280/how-do-i-grant-sudo-privileges-to-an-existing-user

-SSH keys -Digital Oceon & Archlinux
https://www.digitalocean.com/community/tutorials/how-to-configure-ssh-key-based-authentication-on-a-linux-server
https://wiki.archlinux.org/index.php/SSH_keys


+++++++++++++APPLICATION INSTRUCTIONS:

==============================================================
EchoChamber INTRODUCTION:
==============================================================

This is a catalog of music that everyone should hear. The intent is that a user will invite friends with similar tastes or 'good' taste in music to add music that they feel everyone should hear.

EchoChamber has been created using Python, Flask, SqlAlchemy, sqlite, Vagrant, and JQuery.
It employs Google and Facebook for login authentication and authorization.

A user can view music without being logged in, however, will not be able to participate in adding, editing or deleting music.

A user that is logged in will have a unique user id. They will be authorized to any music they wish. They will be authorized also to edit and delete any music that they added. They will not, however, be authorized to edit or delete music that another user has added. Further, if a user A added an artist, but another user B added songs under that artist, user A (or any other user) will not have the authority to delete the artist as long as there are songs by that artist in the database. An Admin table has been added to the database for future use, that will allow the admin to delete any music. This will be possibly implemente in a future release.

