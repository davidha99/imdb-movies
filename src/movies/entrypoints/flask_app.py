from flask import Flask, request, render_template
import psycopg2
from movies import models

app = Flask(__name__)
models.start_mappers()


@app.route("/menu", methods=["GET"])
def get_menu():
    return render_template('menu.html')

@app.route("/recommendations", methods=["GET", "POST"])
def get_recommendations():
    if request.method == "POST":
        preferences = []
        movie_genres = {
            "comedy": 1,
            "drama": 2,
            "sci-fi": 3,
            "romantic": 4,
            "adventure": 5
        }

        if request.form.get("comedy"):
            preferences.append(movie_genres["comedy"])
        if request.form.get("drama"):
            preferences.append(movie_genres["drama"])
        if request.form.get("sci-fi"):
            preferences.append(movie_genres["sci-fi"])
        if request.form.get("romantic"):
            preferences.append(movie_genres["romantic"])
        if request.form.get("adventure"):
            preferences.append(movie_genres["adventure"])
        
        preference_key = ((preferences[0] * preferences[1] * preferences[2]) % 5) + 1

        connection = psycopg2.connect(database = "movies", user = "movies", password = "abc123", host = "postgres", port = "5432")
        cursor = connection.cursor()
        cursor.execute("INSERT INTO MOVIES (movie_id,preference_key,movie_title,rating,year,create_time) \
      VALUES (100, 1, 'El padrino', 7.0, 1999, '2017-08-19 12:17:55 -0400')")
        cursor.execute("SELECT movie_title FROM movies")

        rows = cursor.fetchall()
        return str(rows)


