# PixivURLs
一个获取P站图片地址的工具，后续可能会有更多功能。

## 依赖:
程序是用Python 3编写的，所以请确保你已经安装过Python 3。另外你需要安装pixivpy包，一个简便安装方法如下：
```
pip install pixivpy
```
然后在使用前编辑脚本，更改账号信息为你的账号密码。

## 用法:
```
python user.py [user ID] #获取指定用户的作品
python keywords.py [Keyword] [Minimum Bookmarks] #获取搜索结果
python bookmarks.py #获取公开收藏夹内容
python bookmarksp.py #获取私人收藏夹内容
```
所有结果都会保存到运行目录下的txt文件中。

## 提示:
尽管本程序开源，但是请不要将下载的图片用作商业用途，作品的版权归作者所有。高频率的访问可能导致被拒绝访问，请按照需要自行加入sleep。P站存在防盗链措施，怎么处理看大家自行发挥。
