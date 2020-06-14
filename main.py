import sys
from time import sleep
import requests
if __name__ == "__main__":
    my_urls = (sys.argv[1]).split(',')
    for url in my_urls:
        data=requests.get(url)
        print(data.content)
        sleep(1)
