
This project is for the research that I'm doing at the McGill Shared Reality Lab.
At this point the code here is being use by me to extract the alt text and images from the json files created by the McGill IMAGE chrome plugin.

## Runnning the script

Use the run.py script to extract image and alt text from the raw data generated from the IMAGE plugin.

Steps:
1. Collect the raw data.
    a. You can collect your own data and store it in an individual dir
    b. Use the sample data by unziping `all_data.zip`
2. run `python3 run.py raw_data_paht out_put_path`. If you don't add the `raw_data` or `out_put_path` options, it will default to `./dataset` and `./collected_data` respectively.

3. The script will populate the `out_put_path/images` directory with the images and `out_put_path/captions.json` with the alt text of the images.


### suggested steps
```
git clone https://github.com/namdar-nejad/IMAGE-context
cd IMAGE-context/
unzip all_data.zip
python run.py ./all_data/News/ ./results/news
python run.py ./all_data/Blogs/ ./results/blogs
python run.py ./all_data/Wiki/ ./results/wiki
```


## Dataset
The dataset.zip folder contains 3 directories.
```
dataset
└───Wiki
└───Blogs
└───News
```
Each directory contains about 80 json files collected from using the IMAGE chrome extention from 'wiki', 'news', and 'blog' sources respectivly.

#### Wiki:
The wiki data have been collected from some of the most popular [Fully Protected Wikipedia](https://en.wikipedia.org/wiki/User:West.andrew.g/Popular_pages) Pages.
Some pages that I have used include:
* https://en.wikipedia.org/wiki/Coronavirus
* https://en.wikipedia.org/wiki/Wikipedia
* https://en.wikipedia.org/wiki/United_States
* https://en.wikipedia.org/wiki/Coca-Cola
* https://en.wikipedia.org/wiki/Canada
* https://en.wikipedia.org/wiki/Chicago
* https://en.wikipedia.org/wiki/Climate_change

#### Blog:
For the blog data, I chose a few blogs from the higest ranked blogs on [rankedblogs.com](https://www.rankedblogs.com). A few of them include:
* https://streetartnyc.org/
* https://www.gopetfriendly.com/blog/
* https://www.10adventures.com/blog/
* https://plantsarethestrangestpeople.blogspot.com/
* https://www.sidestreetstyle.com/
* https://www.katheats.com/

#### News:
The news data was collected from [yahoo news](https://www.yahoo.ca).
