import os
from time import sleep
import requests
if __name__ == "__main__":
    urls = os.environ['url_line']
    my_urls=urls.split(',')
    for url in my_urls:
        print(url)
        data=requests.get(url)
        sleep(1)
