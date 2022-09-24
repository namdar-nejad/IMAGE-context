#!/usr/bin/env python
# coding: utf-8

# In[1]:


# import sys
# !{sys.executable} -m pip install --user Html2Image


# In[2]:


FILE_DIR = './dataset'
DATA_DIR = './collected_data'


# In[3]:


import os
import json
import imgkit
import base64
from IPython.core.display import display, HTML
from html2image import Html2Image
from bs4 import BeautifulSoup


# In[4]:


def get_files():
    path = os.path.abspath(FILE_DIR)
    return os.listdir(path)


# In[5]:


def get_json(file_name):
    file_path = os.path.abspath(FILE_DIR+"/"+file_name)
    
    with open(file_path, "r") as file:
        return json.load(file)


# In[6]:


def get_alt(json_):
    context = json_['context']
    soup = BeautifulSoup(context, 'html.parser')
    alt = soup.find('img', alt=True)['alt']
    return alt


# In[7]:


def get_img_html(img_):
    return f"<html> <body> <img src=\"{img_}\"> </body> </html>"

def display_img(html_):
    display(HTML(html_))
    
def save_pic(html_, name, path = f"{DATA_DIR}/images/"):
    hti = Html2Image()
    path_ = os.path.abspath(path)
    hti._output_path = path_
    hti.screenshot(html_str=html_, save_as=name)


# In[8]:


def validateJSON(path):
    return path.endswith(".json")


# In[9]:


def go(dir_=FILE_DIR):
    files = get_files()
    captions = {}
    
    for file, ind in zip(get_files(), range(1, len(files)+1)):
        print(f"{ind}: {file} {validateJSON(file)}")
        
        if validateJSON(file):
            name_ = f'image{ind}.jpg'
            json_ = get_json(file)
            html_ = get_img_html(json_['graphic'])
            txt = get_alt(json_)
            
            if len(txt) > 5:
                captions[name_] = txt
                save_pic(html_, name_)
    
    with open(f"{DATA_DIR}/captions.json", "w") as outfile:
        json.dump(captions, outfile)

