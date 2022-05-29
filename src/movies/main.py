import csv
from typing import List
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Facade import Facade
from InterfacePrintList import InterfacePrintList

from movies.models import get_postgres_uri
from movies.printWithKey1 import printWithKey1
from movies.printWithKey2 import printWithKey2
from movies.printWithKey3 import printWithKey3
from movies.printWithKey4 import printWithKey4

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

    #Backwards - Descending order
    n = len(movie_list)
    for movie in reversed(movie_list):
        title = movie["movie_title"]
        movie_preference_key = movie["preference_key"]
        if user_preference_key == movie_preference_key:
            print(f"{n}: {title}")
            n -= 1

def main():
    preference1, preference2, preference3 = print_menu()
    user_preference_key = algorithm(preference1, preference2, preference3)

    #Interface Segregation - By not communicating directly to the concrete classes, we can assure interface segregation because
    #we will only be able to use methods declared in Facade. If Fetcher had more methods declared, we will not be able to access them

    #Not sure - Dependency Inversion - It is implemented by having communication to the interfaces and not concrete classes, in this
    #example, with facade class. We eliminate dependency between fetcher, downloader and and main class.
    
    # Facade
    facade = Facade()
    facade.download_data()
    list = facade.fetch_movies()

    # Print final movie list from user preferences
    print_recommendations(list, user_preference_key)
 

    #Implementing strategy pattern to print final list to users
    if user_preference_key == 1:
        printing_list = printWithKey1()
    elif user_preference_key == 2:
        printing_list = printWithKey2()
    elif user_preference_key == 3:
        printing_list = printWithKey3()
    elif user_preference_key == 4:
        printing_list = printWithKey4()
    
    InterfacePrintList.printList(printing_list)


    # Factory
    fields = ["preference_key", "movie_title", "star_cast", "rating", "year", "place", "vote", "link"]
    with open("movie_results.csv", "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fields)
        writer.writeheader()
        for movie in list:
            writer.writerow({**movie})

if __name__ == '__main__':
    main()
