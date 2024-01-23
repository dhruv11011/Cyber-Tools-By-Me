import requests
from bs4 import BeautifulSoup
import os

def crawl_website(url, depth=2):
    visited_urls = set()

    def recursive_crawl(current_url, current_depth):
        if current_depth > depth or current_url in visited_urls:
            return

        print(f"Crawling: {current_url}")

        try:
            response = requests.get(current_url)
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                title = soup.title.text if soup.title else 'No title'
                print(f"Title: {title}\n")

                visited_urls.add(current_url)

                for link in soup.find_all('a', href=True):
                    next_url = link['href']
                    if next_url.startswith('http'):
                        recursive_crawl(next_url, current_depth + 1)

        except Exception as e:
            print(f"Error crawling {current_url}: {e}")

    recursive_crawl(url, 0)

if __name__ == "__main__":
    os.system('cls')
    print("\t\tThis is Website  Crawler Tools Made By Dhruv Bhatt")
    target_url = input("Enter the URL to crawl: ")
    crawl_website(target_url)
