#!/usr/bin/env python
# coding: utf-8

# In[1]:


# import sys
# !{sys.executable} -m pip install --user Html2Image


# In[2]:


import os
import json
import imgkit
import base64
import shutil
import logging
from IPython.core.display import display, HTML
from html2image import Html2Image
from bs4 import BeautifulSoup


# In[3]:


# default paths:
RAW_DIR = './dataset'            # dir holding the raw data
OUTPUT_DIR = './collected_data'  # dir holding the image and context should be saved in


# In[4]:


"""
Function to get all the files in a given dir
:my_dir: the dir to check
"""
def get_files(my_dir = RAW_DIR):
    path = os.path.abspath(my_dir)
    return os.listdir(path)


# In[5]:


"""
Given a directory (contaning raw data files) and a file name, the function will return the json of the file
:my_dir: the directory contaning raw data files
:file_name: filename of the file to get
"""
def get_json(file_name, my_dir = RAW_DIR):
    file_path = os.path.abspath(my_dir+"/"+file_name)
    
    with open(file_path, "r") as file:
        return json.load(file)


# In[6]:


"""
Given a json from the raw data, this function will extract the alt text
:my_json: json from raw data
"""
def get_alt(my_json):
    context = my_json['context']
    soup = BeautifulSoup(context, 'html.parser')
    alt = soup.find('img', alt=True)['alt']
    return alt


# In[7]:


"""
Creates the image from the image data
:my_image: image data extracted from the raw data json
"""
def get_img_html(my_image):
    return f"<html> <body> <img src=\"{my_image}\"> </body> </html>"

"""
Given a html image, it dispalys the image
:my_html: a given html string
"""
def display_img(my_html):
    display(HTML(my_html))

"""
Save a html contaning an image to a given location
:my_html: the html to save
:name: name of the to save
:out_dir: directory to save the image to
"""
def save_image(my_html, name, out_dir):

    path_ = os.path.abspath(f"{out_dir}")
    image_b64 = my_html.split(",")[1]
    binary = base64.b64decode(image_b64)
    with open(f"{path_}/{name}.png", "wb") as file:
        file.write(binary)

# In[8]:


"""
Checks if a given paht is a json file
:path: the path to a file to check
"""
def validateJSON(path):
    return path.endswith(".json")

"""
Deletes all files in a given directory
:mydir: the directory to clear
"""
def remove_all_files(mydir):
    for f in os.listdir(mydir):
        os.remove(os.path.join(mydir, f))


# In[9]:

def go(raw_dir=RAW_DIR, output_dir=OUTPUT_DIR):
    
    # logger
    logging.basicConfig(filename=f"{output_dir}/log.log", level=logging.INFO, filemode='w')
    
    image_dir = f"/{output_dir}/images"  # dir to save the images
    files = get_files(raw_dir)            # list of raw data files
    captions = {}                         # dict to store the captions
    no_alt, error = 0, 0
    
    # clear the image dir
    if os.path.exists(image_dir):
        remove_all_files(image_dir)
        
    logging.info(f"[LOG] data_dir = {image_dir}, out_put_dir = {output_dir}")
    logging.info(f"[LOG] {len(files)} raw data files detected")
    
    for file, ind in zip(files, range(1, len(files)+1)):
        logging.info(f"[LOG] working on file {ind}: {file}")
        if validateJSON(file):
            try:
                name_ = f'image{ind}'
                json_ = get_json(file_name = file, my_dir = raw_dir)
                html_ = get_img_html(json_['graphic'])
                txt = get_alt(json_)
                
                if len(txt) > 2:
                    captions[name_] = txt
                    save_image(html_, name_+".png", output_dir)
                    logging.info(f"[COMPLETED] {ind}: {file} no alt txt")
                    
                else:
                    no_alt += 1
                    logging.info(f"[FAILED] {ind}: {file} no alt txt")
                    
            except Exception as e:
                error += 1
                logging.info(f"[FAILED] {ind}: {file} ERROR {str(e)}")
        else:
            logging.info(f"[FAILED] {ind}: {file} not a json file")
    
    
    with open(f"{output_dir}/captions.json", "w") as outfile:
        json.dump(captions, outfile)
    
    logging.info(f"total: {len(files)}")
    logging.info(f"completed: {len(captions)}")
    logging.info(f"no_alt: {no_alt}")
    logging.info(f"error: {error}")
    
    logging.shutdown()
