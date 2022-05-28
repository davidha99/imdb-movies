import csv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Facade import Facade

from movies.models import get_postgres_uri

DEFAULT_SESSION_FACTORY = sessionmaker(
    bind=create_engine(
        get_postgres_uri(),
        isolation_level="REPEATABLE READ",
    )
)
session = DEFAULT_SESSION_FACTORY()


def main():

    #Interface Segregation - By not communicating directly to the concrete classes, we can assure interface segregation because
    #we will only be able to use methods declared in Facade. If Fetcher had more methods declared, we will not be able to access them

    #Check about Dependency Inversion
    
    # Facade
    facade = Facade()
    facade.download_data()
    list = facade.fetch_movies()

    # Factory
    fields = ["preference_key", "movie_title", "star_cast", "rating", "year", "place", "vote", "link"]
    with open("movie_results.csv", "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fields)
        writer.writeheader()
        for movie in list:
            writer.writerow({**movie})

if __name__ == '__main__':
    main()
