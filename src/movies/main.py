import csv
from typing import List
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Facade import Facade
from movies.printService import printService
from printAsc import printAsc
from printDesc import printDesc
from movies.Downloader import Downloader
from movies.Fetcher import Fetcher
import pandas

from movies.models import get_postgres_uri

DEFAULT_SESSION_FACTORY = sessionmaker(
    bind=create_engine(
        get_postgres_uri(),
        isolation_level="REPEATABLE READ",
    )
)
session = DEFAULT_SESSION_FACTORY()


def algorithm(p1: int, p2: int, p3: int) -> int:
    return ((p1 * p2 * p3) % 5) + 1

def movie_fetch():

    # Design principle: Interface Segregation - By not communicating directly to the concrete classes, we can assure interface segregation because
    #we will only be able to use methods declared in Facade. If Fetcher had more methods declared, we will not be able to access them
    
    # Design pattern: Facade
    # Design principle: Dependency Inversion - Facade class comunicates through Downloader and Fetcher interfaces and doesn't have dependencies
    downloader = Downloader()
    fetcher = Fetcher()
    facade = Facade(downloader, fetcher)
    facade.download_data()
    list = facade.fetch_movies()

    fields = ["preference_key", "movie_title", "star_cast", "rating", "year", "place", "vote", "link"]
    with open("/src/movies/movie_results.csv", "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fields)
        writer.writeheader()
        for movie in list:
            writer.writerow({**movie})

# Design Pattern: Strategy - We abstract away an algorithm so that we can configure our context (printService)
# We change the behavior of our context based on the rating parameter
def strategy(rating: bool, preference_key: int) -> List:
    preference_movies = []

    if not rating:
        printOrder = printAsc(preference_key)
    else:
        printOrder = printDesc(preference_key)

    service = printService(printOrder)
    preference_movies = service.print()

    return preference_movies

if __name__ == '__main__':
    movie_fetch()
