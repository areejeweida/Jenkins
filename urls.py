import requests
from bs4 import BeautifulSoup
import sys


def main():
    urls = sys.argv[1]
    for url in urls.split(","):
        page = requests.get(url)
        soup = BeautifulSoup(page.content, "html.parser")
        print(soup)


if __name__ == '__main__':
    main()
