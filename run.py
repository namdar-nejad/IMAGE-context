from data import *
import sys

if __name__ == "__main__":
    if len(sys.argv) > 1:
        go(file_path = sys.argv[1])
    else:
        go()
