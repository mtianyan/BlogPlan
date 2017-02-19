'''
鐖櫕鎺у埗妯″潡
璋冪敤鍏朵粬妯″潡瀹屾垚鏁版嵁鎶撳彇
'''

import url_manager, html_downloader, html_parser, html_outputer


class SpiderMain(object):
    def __init__(self):
        self.maxcount = 100  # 鎶撳彇鏁版嵁鏁伴噺
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()

    def craw(self, root_url):
        count = 0
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                html_cont = self.downloader.download(new_url)
                new_urls, new_data = self.parser.parse(new_url, html_cont)
                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_data)

                if count == self.maxcount:
                    break
            except Exception as e:
                print(e)
                continue
            else:
                count += 1
                print(new_url)

        self.outputer.output_html()  # 鍐呭杈撳嚭鑷虫枃浠�


# 绋嬪簭鍏ュ彛
if __name__ == '__main__':
    root_url = 'http://baike.baidu.com/view/21087.htm'  # 璧峰鐩爣
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)
