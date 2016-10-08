import mechanicalsoup
import requests
import string
import os
import sys

def format_filename(s):
    valid_chars = "-_.() %s%s" % (string.ascii_letters, string.digits)
    filename = ''.join(c for c in s if c in valid_chars)
    filename = filename.replace(' ','-') # I don't like spaces in filenames.
    return filename

def get_page(url):
    browser = mechanicalsoup.Browser(soup_config={"features":"html.parser"})
    page = browser.get(url)
    return (browser, page)

def download_file(filename, url):
    # This should not be here...
    if os.path.exists(filename):
        print('Already downloaded: {}'.format(filename))
        return filename

    print('Downloading: {} ({})'.format(filename, url))
    r = requests.get(url, stream=True)
    with open(filename, 'wb') as f:
        total_length = int(r.headers.get('content-length'))
        dl = 0
        bar_length = 100
        for chunk in r.iter_content(chunk_size=4096):
            if chunk:
                dl += len(chunk)
                done = int(bar_length * dl / total_length)
                f.write(chunk)
                sys.stdout.write("\r[{}{}] {}%".format('=' * done, ' ' * (bar_length-done), round(dl / float(total_length) * 100, 1)))
                sys.stdout.flush()
    print("")
    return filename