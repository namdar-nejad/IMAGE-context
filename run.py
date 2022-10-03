from extract_data import *
import sys

if __name__ == "__main__":
    if len(sys.argv) == 2:
        go(raw_dir = sys.argv[1])
    elif len(sys.argv) == 3:
        go(raw_dir = sys.argv[1], output_dir=sys.argv[2])
    else:
        go()