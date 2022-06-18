from flask import Flask, request, render_template
import pandas
from movies import models

app = Flask(__name__)
models.start_mappers()


@app.route("/menu", methods=["GET"])
def get_menu():
    return render_template('menu.html')

@app.route("/recommendations", methods=["GET", "POST"])
def get_recommendations():
    if request.method == "POST":
        count = 0
        preferences = []
        movie_genres = {
            "comedy": 1,
            "drama": 2,
            "sci-fi": 3,
            "romantic": 4,
            "adventure": 5
        }

        if request.form.get("comedy"):
            count += 1
            preferences.append(movie_genres["comedy"])
        if request.form.get("drama"):
            count += 1
            preferences.append(movie_genres["drama"])
        if request.form.get("sci-fi"):
            count += 1
            preferences.append(movie_genres["sci-fi"])
        if request.form.get("romantic"):
            count += 1
            preferences.append(movie_genres["romantic"])
        if request.form.get("adventure"):
            count += 1
            preferences.append(movie_genres["adventure"])
        if count != 3:
            return "<h1>Solo se pueden seleccionar 3 preferencias</h1>", 200
        
        preference_key = ((preferences[0] * preferences[1] * preferences[2]) % 5) + 1

        # Tratamos de hacer de obtener los datos de la base de datos, pero la tabla no
        # está poblada y la tendríamos que poblar nosotros. Por lo que, optamos obtener
        # los datos desde el archivo movie_results.csv

    #     connection = psycopg2.connect(database = "movies", user = "movies", password = "abc123", host = "postgres", port = "5432")
    #     cursor = connection.cursor()
    #     cursor.execute("INSERT INTO MOVIES (movie_id,preference_key,movie_title,rating,year,create_time) \
    #   VALUES (100, 1, 'El padrino', 7.0, 1999, '2017-08-19 12:17:55 -0400')")
    #     cursor.execute("SELECT movie_title FROM movies")

        # rows = cursor.fetchall()

        file = pandas.read_csv("/src/movies/movie_results.csv")
        all_movies = list(file.iloc[:,1].values)
        preference_keys = list(file.iloc[:,0].values)
        preference_movies = []

        for i in range(len(all_movies)):
            if preference_keys[i] == preference_key:
                preference_movies.append(all_movies[i])

        return render_template("recommendations.html", preference_movies=preference_movies)
        



