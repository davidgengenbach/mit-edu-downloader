#!/usr/bin/env python3

import sys
import helper
from urllib.parse import urlparse

if len(sys.argv) < 2:
    print("Usage: {} url".format(sys.argv[0]))
    sys.exit(1)


URL = sys.argv[1]
(browser, page) = helper.get_page(URL)

DOMAIN = "{uri.scheme}://{uri.netloc}".format(uri=urlparse(URL))

lecture_links = page.soup.select('a.medialink')
for index, lecture_link in enumerate(lecture_links):
    link = "{}/{}".format(DOMAIN, lecture_link.attrs['href'])
    video_page = browser.get(link)
    sub_headlines = video_page.soup.select('h2.subhead')
    for headline in sub_headlines:
        if 'Free Downloads' in headline:
            video_links = headline.parent.select('a')
            video_link = video_links[1].attrs['href']
            print(video_link)
    #print(video_links)
    #
