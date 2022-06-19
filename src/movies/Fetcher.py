# Design principle: Single Responsability Principle - The fetcher is responsible for the 
# movies' information extraction

from typing import List
import re
from Downloader import Downloader
from InterfaceFetcher import InterfaceFetcher

class Fetcher(InterfaceFetcher):        
    def fetch_movies(self, downloader : Downloader) -> List:
        # create an empty list for storing
        # movie information
        list = []

        # Get data from Downloader getters
        movies = downloader.movies
        links = downloader.links
        crew = downloader.crew
        ratings = downloader.rating
        votes = downloader.votes

        # Iterating over movies to extract
        # each movie's details
        for index in range(0, len(movies)):
            # Separating movie into: 'place',
            # 'title', 'year'
            movie_string = movies[index].get_text()
            movie = (' '.join(movie_string.split()).replace('.', ''))
            movie_title = movie[len(str(index)) + 1:-7]
            year = re.search('\((.*?)\)', movie_string).group(1)
            place = movie[:len(str(index)) - (len(movie))]

            data = {"movie_title": movie_title,
                    "year": year,
                    "place": place,
                    "star_cast": crew[index],
                    "rating": ratings[index],
                    "vote": votes[index],
                    "link": links[index],
                    "preference_key": index % 4 + 1}
            list.append(data)
        
        return list
        


