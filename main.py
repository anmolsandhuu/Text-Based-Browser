import argparse
import os
import requests
from bs4 import BeautifulSoup

ap = argparse.ArgumentParser()
ap.add_argument('dir', nargs='?', help='Directory for tab')
args = ap.parse_args()
_dir_ = args.dir

tags = ('p', 'a', 'ul', 'ol', 'li', 'h1', 'h2', 'h3', 'h4')
visited_pages = set()
user_history = []


def url_validate(url):
    return url.find('.') != -1


def url_to_tab(url):
    return url.split('.')[0]


def page_visit(url):
    with open(f'{os.path.join(_dir_, url_to_tab(url))}.txt', 'w+') as tab:
        print(make_request(url), file=tab)

        user_history.append(url)
        visited_pages.add(url_to_tab(url))


def show_page_visit(tab):
    with open(f'{os.path.join(_dir_, url_to_tab(tab))}.txt', 'r') as tab:
        print(tab.read())


def make_request(url):
    url = "https://" + url
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    p = soup.find_all(tags)
    return ''.join([x.get_text() for x in p])


if _dir_:
    try:
        os.makedirs(_dir_)
    except FileExistsError:
        pass

while True:
    user_input = input()
    if user_input == 'exit':
        exit(1)
    elif user_input == 'back':
        if len(user_history) == 0:
            print('NO HISTORY FOUND')
        else:
            try:
                show_page_visit(user_history.pop(-2))
            except:
                print('history out of index')
            finally:
                print('No other history found')
    elif user_input in visited_pages:
        show_page_visit(user_input)
    elif url_validate(user_input):
        page_visit(user_input)
        show_page_visit(user_input)
    else:
        print('error: Incorrect URl')
