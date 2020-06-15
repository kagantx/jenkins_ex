import os
from time import sleep
import requests
if __name__ == "__main__":
    urls = os.environ['MYVAR']
    my_urls=urls.split(',')
    for url in my_urls:
        data=requests.get(url)
        print(data.content)
        sleep(1)
