Script to extract image and alt text from the raw data generated from the IMAGE plugin.

Steps:
1. Collect the raw data.
    a. You can collect your own data and store it in an individual dir
    b. Use the sample data by unziping `all_data.zip`
2. run `python3 run.py raw_data_paht out_put_path`. If you don't add the `raw_data` or `out_put_path` options, it will default to `./dataset` and `./collected_data` respectively.

3. The script will populate the `out_put_path\images` directory with the images and `out_put_path\captions.json` with the alt text of the images.

### suggested steps
```
git clone https://github.com/namdar-nejad/IMAGE-context
cd IMAGE-context/
unzip all_data.zip
python run.py ./all_data/News/ ./results/news
python run.py ./all_data/Blogs/ ./results/blogs
python run.py ./all_data/Wiki/ ./results/wiki
```
