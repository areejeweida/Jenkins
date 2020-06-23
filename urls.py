import sys
import urllib.request

urls = sys.argv[1]
urls = urls.split(',')

for url in urls:
    html_ = urllib.request.Request(url)
    print(html_.text)
