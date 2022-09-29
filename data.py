#!/usr/bin/env python
# coding: utf-8

# In[13]:


# import sys
# !{sys.executable} -m pip install --user Html2Image


# In[1]:


import os
import json
import imgkit
import base64
import shutil
import logging
from IPython.core.display import display, HTML
from html2image import Html2Image
from bs4 import BeautifulSoup


# In[2]:


FILE_DIR = './dataset'
DATA_DIR = './collected_data'
logging.basicConfig(filename=f"{DATA_DIR}/log.log", level=logging.INFO, filemode='w')


# In[3]:


def get_files():
    path = os.path.abspath(FILE_DIR)
    return os.listdir(path)


# In[4]:


def get_json(file_name):
    file_path = os.path.abspath(FILE_DIR+"/"+file_name)
    
    with open(file_path, "r") as file:
        return json.load(file)


# In[5]:


def get_alt(json_):
    context = json_['context']
    soup = BeautifulSoup(context, 'html.parser')
    alt = soup.find('img', alt=True)['alt']
    return alt


# In[6]:


def get_img_html(img_):
    return f"<html> <body> <img src=\"{img_}\"> </body> </html>"

def display_img(html_):
    display(HTML(html_))
    
def save_pic(html_, name, path = f"{DATA_DIR}/images/"):
    hti = Html2Image()
    path_ = os.path.abspath(path)
    hti._output_path = path_
    hti.screenshot(html_str=html_, save_as=name)


# In[7]:


def validateJSON(path):
    return path.endswith(".json")

def remove_all_files(mydir):
    for f in os.listdir(mydir):
        os.remove(os.path.join(mydir, f))


# In[8]:


def go(dir_=FILE_DIR):
    files = get_files()
    captions = {}
    image_dir = f"./{DATA_DIR}/images"
    
    if os.path.exists(image_dir):
        remove_all_files(image_dir)
    
    for file, ind in zip(get_files(), range(1, len(files)+1)):        
        if validateJSON(file):
            try:
                name_ = f'image{ind}.jpg'
                json_ = get_json(file)
                html_ = get_img_html(json_['graphic'])
                txt = get_alt(json_)

                if len(txt) > 5:
                    captions[name_] = txt
                    save_pic(html_, name_)
                else:
                    logging.info(f"skipped {ind}: {file} no alt txt")
                    print(f"skipped {ind}: {file} no alt txt")
            except Exception as e:
                logging.info(f"skipped {ind}: {file} ERROR {str(e)}")
                print(f"skipped {ind}: {file} ERROR {str(e)}")
            
        else:
            logging.info(f"skipped {ind}: {file} not json")
            print(f"skipped {ind}: {file} not json")
    
    with open(f"{DATA_DIR}/captions.json", "w") as outfile:
        json.dump(captions, outfile)
        
    logging.shutdown()


# In[ ]:




