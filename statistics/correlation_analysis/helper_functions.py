import os
import sys

def add_path_until_readme():
    current_dir = './'
    count = 0
    max_count = 10
    while (count < max_count and not ('README.md' in os.listdir(current_dir))):
        current_dir += '../'
        count += 1
    if count == max_count:
        raise Exception('Could not find README.md')
    else:
        sys.path.append(os.path.abspath(current_dir))
        return current_dir

# pull get helper code    
add_path_until_readme()
from helper_code.print_image import *