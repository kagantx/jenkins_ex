import os
from time import sleep
import requests
if __name__ == "__main__":
    my_urls = os.environ['MYVAR']
    print(my_urls)
    for url in my_urls:
        data=requests.get(url)
        print(data.content)
        sleep(1)
