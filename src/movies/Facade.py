from Fetcher import Fetcher
from Downloader import Downloader

class Facade:
    def download_data(self):
        Downloader.download()

    def fetch_movies(self):
        return Fetcher.fetch_movies()