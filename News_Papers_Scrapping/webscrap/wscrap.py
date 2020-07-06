from urllib.request import urlopen

import self as self
from bs4 import BeautifulSoup

# Global Variable
url_aj = "https://www.somoynews.tv/"
filepath = "html/aj.html"


class NewsScraper:
    _url = ''
    _data = ''
    _wlog = None
    _soup = None

    def __init__(self, url, wlog):
        self._url = url
        self._wlog = wlog

    def retrieve_webpage(self):
        try:
            html = urlopen(self._url)
        except Exception as e:
            print(e)
            self._wlog.report(e)
        else:
            self._data = html.read()
            if len(self._data) > 0:
                print('Successfully Retrive')

    def write_webpage_as_html(self, filepath=filepath, data=''):
        try:
            with open(filepath, 'wb') as fobj:
                if data:
                    fobj.write(data)
                else:
                    fobj.write(self._data)
        except Exception as e:
            print(e)
            self._wlog.report(str(e))

    def read_webpage_from_html(self, filepath=filepath):
        try:
            with open(filepath) as fobj:
                self._data = fobj.read()
        except Exception as e:
            print(e)
            self._wlog.report(str(e))

    def change_url(self, url):
        self._url = url

    def print_data(self):
        print(self._data)

    def convert_data_to_bs4(self):
        self._soup = BeautifulSoup(self._data, "html.parser")

    def parse_soup_to_simple_html(self):
        news_list = self._soup.find_all(['h1', 'h2', 'h3', 'h4'])  # h1

        # print (news_list)

        htmltext = '''
    <html>
        <head><title>Simple News Link Scrapper</title></head>
        <body>
            {NEWS_LINKS}
        </body>
    </html>
    '''

        news_links = '<ol>'

        for tag in news_list:
            if tag.parent.get('href'):
                link = self._url + tag.parent.get('href')
                title = tag.string
                news_links += "<li><a href='{}' target='_blank'>{}</a></li>\n".format(link, title)

                news_links += '</ol>'
                htmltext = htmltext.format(NEWS_LINKS=news_links)

                # print(htmltext)
                self.write_webpage_as_html(filepath="html/simplenews.html", data=htmltext.encode())
