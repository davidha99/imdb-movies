import random
from InterfacePrintList import InterfacePrintList
import pandas

class printDesc(InterfacePrintList):
    def __init__(self, preference_key) -> None:
        self.preference_key = preference_key

    def printList(self):
        # Read CSV file: get movie title column and preference key column
        file = pandas.read_csv("/src/movies/movie_results.csv")
        preference_keys = list(file.iloc[:,0].values)
        all_movies = list(file.iloc[:,1].values)
        all_ratings = list(file.iloc[:,3].values)
        
        preference_movies = [] # Has all movies with preference key
        recommendations = []
        
        for i in range(len(all_movies)):
            if preference_keys[i] == self.preference_key:
                preference_movies.append((all_movies[i], all_ratings[i]))

        # preference_movies = [('perro', 9.8), ('gato', 5), ('hola', 8)]
        # lista = {1:0}

        lista = {}
        for i in range(10):
            index = random.randint(0, len(preference_movies))
            while(index in lista.keys()):
                index = random.randint(0, len(preference_movies)) 
            lista[index] = 1

            recommendations.append((preference_movies[index][0], preference_movies[index][1]))

        # new_list = []
        # for i in range(len(recommendations)):
        #     new_list.append(recommendations[i][0])

        return sorted(recommendations, key=lambda tup: tup[1], reverse=True)