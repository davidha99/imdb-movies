from Fetcher import Fetcher
from Downloader import Downloader

class Facade:
    def __init__(self, downloader, fetcher) -> None:
        self.downloader = downloader
        self.fetcher = fetcher

    def download_data(self):
        self.downloader.download()

    def fetch_movies(self):
        return self.fetcher.fetch_movies(self.downloader)