# SoundScapes 
<hr>
SoundScapes is a django music platform app that delivers an immersive and personalized audio experience to music enthusiasts worldwide. Whether you're a casual listener, a passionate music explorer, or an artist seeking a platform to showcase your talent, SoundScapes has something extraordinary to offer.



## Table of Contents

- [Installation](#installation-)
- [Features](#features)
- [Contributing](#contributing)
- [Badges](#badges)

## Installation 

First make a python virtual environment and install requirements from requirements.txt

```bash
pip install -r requirements.txt
``` 
Then active database .we comment postgresql setting in settings.py if you want to work with postgresql but our default is sqlite db.
```bash
python manage.py makemigrations
python manage.py migrate
``` 
To run project :
```bash
python manage.py runserver
``` 
Then if you want you can add some datas on project you can log in to django admin (http://127.0.0.1:8000/admin/). First you should create a superuser.
```bash
python manage.py createsuperuser
``` 
## Features
Audio: Enjoy your favorite tracks in high-quality audio, providing a superior listening experience that captures the nuances of each note.

Login and Register: Create a personalized account to unlock additional features. Log in securely to access your saved playlists, preferences, and enjoy a seamless experience across devices.

Favorites: Mark your favorite songs or playlists with a simple click. Easily access and enjoy your most-loved music whenever you want.

Follow and Expand Connections: Connect with other music enthusiasts by following their profiles. Expand your musical connections, discover new content, and stay updated on what others are listening to.

Artist Profiles: Explore detailed profiles of your favorite artists, learn about their journey, and stay updated on their latest releases and activities.

## Contributing

If you want to contribute yo our project. follow instructions bellow :
1. Fork the repository
3. Make changes and commit them (`git commit -am 'Add <feature'>`)
4. Push (`git push origin`)
5. Create a pull request


## Badges
![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white) ![Celery](https://img.shields.io/badge/celery-%23a9cc54.svg?style=for-the-badge&logo=celery&logoColor=ddf4a4) ![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white) ![RabbitMQ](https://img.shields.io/badge/Rabbitmq-FF6600?style=for-the-badge&logo=rabbitmq&logoColor=white)


Thanks to this beautiful kind persons . we got some helps and ideas :
1.https://github.com/manjurulhoque/django-music-streaming-app 
2.https://github.com/varadbhogayata/music-player/tree/master
3.https://colorlib.com/wp/templates/


if you found bug or anything let us know :
faridkiaeieh@gmail.com

And finally if you liked this project . make our day with a star 😃❤️ 

