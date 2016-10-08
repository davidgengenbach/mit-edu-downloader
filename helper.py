import mechanicalsoup


def get_page(url):
    browser = mechanicalsoup.Browser(soup_config={"features":"html.parser"})
    page = browser.get(url)
    return (browser, page)