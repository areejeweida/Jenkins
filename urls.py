import sys
import requests

urls = sys.argv[1]
urls = urls.split(',')

for url in urls:
    html_ = requests.get(url)
    print(html_.text)
