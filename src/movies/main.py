import csv
from typing import List
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

def print_menu():
    print("-----------------------------------------------")
    print("1. Comedy")
    print("2. Drama")
    print("3. Sci-fi")
    print("4. Romantic")
    print("5. Adventure")
    print("-----------------------------------------------")
    preference1 = int(input("Choose preference 1 (1,2,3,4,5): "))
    preference2 = int(input("Choose preference 2 (1,2,3,4,5): "))
    preference3 = int(input("Choose preference 3 (1,2,3,4,5): "))
    return preference1, preference2, preference3

def algorithm(p1: int, p2: int, p3: int) -> int:
    return ((p1 * p2 * p3) % 5) + 1

def print_recommendations(movie_list: List, user_preference_key: int) -> None:
    n = 1
    for movie in movie_list:
        title = movie["movie_title"]
        movie_preference_key = movie["preference_key"]
        if user_preference_key == movie_preference_key:
            print(f"{n}: {title}")
            n += 1

def main():
    preference1, preference2, preference3 = print_menu()
    user_preference_key = algorithm(preference1, preference2, preference3)

    #Interface Segregation - By not communicating directly to the concrete classes, we can assure interface segregation because
    #we will only be able to use methods declared in Facade. If Fetcher had more methods declared, we will not be able to access them

    #Check about Dependency Inversion
    
    # Facade
    facade = Facade()
    facade.download_data()
    list = facade.fetch_movies()

    # Print final movie list from user preferences
    print_recommendations()

    # Factory
    fields = ["preference_key", "movie_title", "star_cast", "rating", "year", "place", "vote", "link"]
    with open("movie_results.csv", "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fields)
        writer.writeheader()
        for movie in list:
            writer.writerow({**movie})

if __name__ == '__main__':
    main()
