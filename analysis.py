import pandas as pd
from IPython.display import display
import sys

wiki_path = sys.argv[1]
news_path = sys.argv[2]
blogs_path = sys.argv[3]

df_wiki = pd.read_json(wiki_path).T
df_news = pd.read_json(news_path).T
df_blogs = pd.read_json(blogs_path).T

describe = pd.DataFrame()
describe['wiki'] = df_wiki['CLIPScore'].describe()
describe['blogs'] = df_blogs['CLIPScore'].describe()
describe['news'] = df_news['CLIPScore'].describe()

display(describe)
