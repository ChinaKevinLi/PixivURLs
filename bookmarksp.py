import sys
from pixivpy3 import AppPixivAPI

username="pixiv username"
password="pixiv password"

def get_imageUrls(aapi):
    json_result = aapi.user_bookmarks_illust(aapi.user_id,restrict='private')
    while 1:
        try:
            nLen = len(json_result.illusts)
        except Exception as e:
            print(e)

        for illust in json_result.illusts:
            yield illust

            if illust.page_count == 1 and illust.type != 'ugoira':
                print(illust.meta_single_page.original_image_url)
                print('Bookmarks:' + str(illust.total_bookmarks))
                with open('bookmarks_pri.txt','a+') as f:
                    f.write(illust.meta_single_page.original_image_url+'\n')
                pass
            elif illust.page_count > 1:
                image_urls = [
                    page.image_urls.original
                    for page in illust.meta_pages
                    ]
                print(image_urls)
                print('Bookmarks:' + str(illust.total_bookmarks))
                for url in image_urls:
                    with open('bookmarks_pri.txt','a+') as f:
                        f.write(url+'\n')
            else:
                image_urls = []

        try:
            next_qs = aapi.parse_qs(json_result.next_url)
            if next_qs is None:
                break
            json_result = aapi.user_bookmarks_illust(**next_qs)
        except Exception as e:
            print(e)
            break

    return 1

def main():
    aapi = AppPixivAPI()
    aapi.login(username, password)
    illust_ids = set()
    for illust in get_imageUrls(aapi):
        illust_ids.add(illust.id)

    print('Images Found:'+str(len(illust_ids)))


if __name__ == '__main__':
    main()
