# SRP - El downloader es responsable de descargar los datos de la aplicación web
# de IMDb

from bs4 import BeautifulSoup
from InterfaceDownloader import InterfaceDownloader
import requests

class Downloader(InterfaceDownloader):
    def __init__(self) -> None:
        self.__movies = None
        self.__links = None
        self.__crew = None
        self.__rating = None
        self.__votes = None
    
    @property
    def movies(self):
        return self.__movies
    
    @property
    def links(self):
        return self.__links

    @property
    def crew(self):
        return self.__crew

    @property
    def rating(self):
        return self.__rating

    @property
    def votes(self):
        return self.__votes

    def download(self) -> None:
        # Downloading imdb top 250 movie's data
        url = 'http://www.imdb.com/chart/top'
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'lxml')

        self.__movies = soup.select('td.titleColumn')
        self.__links = [a.attrs.get('href') for a in soup.select('td.titleColumn a')]
        self.__crew = [a.attrs.get('title') for a in soup.select('td.titleColumn a')]
        self.__rating = [b.attrs.get('data-value') for b in soup.select('td.posterColumn span[name=ir]')]
        self.__votes = [b.attrs.get('data-value') for b in soup.select('td.ratingColumn strong')]
    
    