# PixivURLs
An awesome tool to get Pixiv image URLs by specific keywords or user IDs.

## Requirements
Before you use it, please asure that you already have Python 3 on your device and installed pixivpy.You can install it by pip.
```
pip install pixivpy
```
Then you should put your pixiv account infomation into user.py and keyword.py. Jusy edit variables named username and password.

## Usage:
```
python user.py [user ID] 
python keyword.py [Keyword] [Minimum Bookmarks]
```
All URLs will be put in a file named 'url.txt'.
