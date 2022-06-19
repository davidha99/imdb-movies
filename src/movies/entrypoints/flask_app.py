from flask import Flask, request, render_template
from movies import models
from main import movie_fetch, algorithm, strategy

app = Flask(__name__)
models.start_mappers()


@app.route("/menu", methods=["GET"])
def get_menu():
    return render_template('menu.html')

@app.route("/recommendations", methods=["GET", "POST"])
def get_recommendations():
    if request.method == "POST":
        genre_counter = 0
        preferences = []
        movie_genres = {
            "comedy": 1,
            "drama": 2,
            "sci-fi": 3,
            "romantic": 4,
            "adventure": 5
        }

        if request.form.get("comedy"):
            genre_counter += 1
            preferences.append(movie_genres["comedy"])
        if request.form.get("drama"):
            genre_counter += 1
            preferences.append(movie_genres["drama"])
        if request.form.get("sci-fi"):
            genre_counter += 1
            preferences.append(movie_genres["sci-fi"])
        if request.form.get("romantic"):
            genre_counter += 1
            preferences.append(movie_genres["romantic"])
        if request.form.get("adventure"):
            genre_counter += 1
            preferences.append(movie_genres["adventure"])
        if genre_counter != 3:
            return "<h1>Solo se pueden seleccionar 3 preferencias</h1>", 200
        
        preference_key = algorithm(preferences[0], preferences[1], preferences[2])

        movie_fetch()

        rating = True if request.form.get("rating") else False

        preference_movies = strategy(rating, preference_key)

        return render_template("recommendations.html", preference_movies=preference_movies)
        



