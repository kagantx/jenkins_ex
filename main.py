import sys
from time import sleep

if __name__ == "__main__":
    my_input = int(sys.argv[1])
    for num in range(my_input):
        print(num, num * num)
        sleep(1)
