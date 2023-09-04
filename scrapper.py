import requests
from bs4 import BeautifulSoup
from typing import List, Dict
from tqdm import tqdm
import time


class MovieScraper:
    BASE_URL = "https://www.1tamilmv.nexus"
    PAGE_PATH = "/index.php?/forums/forum/11-web-hd-itunes-hd-bluray/page/"
    HEADERS = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/89.0.4389.82 Safari/537.36"
    }

    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update(self.HEADERS)

    def fetch_webpage_content(self, url: str) -> BeautifulSoup:
        response = self.session.get(url)
        response.raise_for_status()  # This will raise an HTTPError if the HTTP request returned an unsuccessful status code
        return BeautifulSoup(response.text, 'html.parser')

    @staticmethod
    def extract_movies(soup: BeautifulSoup) -> List[BeautifulSoup]:
        return soup.findAll('span', {'class': 'ipsType_break ipsContained'})

    @staticmethod
    def extract_movie_title(movie_tag: BeautifulSoup) -> str:
        return movie_tag.select_one('a > span').text.strip().lower()

    @staticmethod
    def extract_movie_link(movie_tag: BeautifulSoup) -> str:
        return movie_tag.find('a')['href']

    def filter_movies_by_name(self, name: str, movies: List[BeautifulSoup]) -> List[BeautifulSoup]:
        return [movie for movie in movies if name in self.extract_movie_title(movie)]

    def scrape_movie_links(self, movie_name: str, num_pages: int) -> List[Dict[str, str]]:
        movie_links = []
        for page in tqdm(range(1, num_pages + 1), desc="Scraping pages", ncols=100):
            url = f"{self.BASE_URL}{self.PAGE_PATH}{page}"
            page_content = self.fetch_webpage_content(url)
            movie_tags = self.extract_movies(page_content)
            relevant_movies = self.filter_movies_by_name(movie_name, movie_tags)
            for movie in relevant_movies:
                title = self.extract_movie_title(movie)
                link = self.extract_movie_link(movie)
                movie_links.append({"title": title, "link": link})
            time.sleep(1)  # Respectful scraping by sleeping for 1 second between requests

        return movie_links


if __name__ == "__main__":
    scraper = MovieScraper()
    movie_name_input = input("Enter the name of the movie you want to search for: ").lower()
    num_pages = int(input("Enter the number of pages you want to scrape: "))
    found_links = scraper.scrape_movie_links(movie_name_input, num_pages)

    for movie in found_links:
        print(f"{movie['title']} : {movie['link']}")
