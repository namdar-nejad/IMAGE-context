from extract_data import *
from os.path import dirname, abspath
import sys

output_dir = dirname(dirname(abspath(__file__)))+'/collected_data'
image_path = dirname(dirname(abspath(__file__)))+'/collected_data/images'

if __name__ == "__main__":
    if len(sys.argv) == 2:
        go(raw_dir = sys.argv[1])
    elif len(sys.argv) == 3:
        output_dir = os.path.abspath(sys.argv[2])
        image_path = os.path.abspath(sys.argv[2] + "/images")
        
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        if not os.path.exists(image_path):
            os.mkdir(image_path)
            
        go(raw_dir = sys.argv[1], output_dir=output_dir)
    else:
        go()
