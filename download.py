#!/usr/bin/env python3

import sys
import helper
import re
from urllib.parse import urlparse

if len(sys.argv) < 2:
    print("Usage: {} url".format(sys.argv[0]))
    sys.exit(1)


URL = sys.argv[1]
(browser, page) = helper.get_page(URL)

DOMAIN = "{uri.scheme}://{uri.netloc}".format(uri=urlparse(URL))

lecture_links = page.soup.select('a.medialink')
for index, lecture_link in enumerate(lecture_links):
    lecture_title = lecture_link.string
    link = "{}/{}".format(DOMAIN, lecture_link.attrs['href'])
    video_page = browser.get(link)

    script = [script for script in video_page.soup.select('script') if 'ocw_embed_chapter_media' in str(script)]
    if len(script) < 1:
        print(":(")
        continue
    youtube_url = re.findall(r'(https:\/\/www.youtube.com\/v\/.*?)\'', str(script[0]))
    if len(youtube_url) < 1:
        print(':((')
        continue
    youtube_url = youtube_url[0]
    print("Downloading: {:<40}\n{}\n".format(lecture_title, youtube_url))

