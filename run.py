from extract_data import *
import sys

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