import argparse
import os

nytimes_com = '''
This New Liquid Is Magnetic, and Mesmerizing
 
Scientists have created “soft” magnets that can flow 
and change shape, and that could be a boon to medicine 
and robotics. (Source: New York Times)
 
 
Most Wikipedia Profiles Are of Men. This Scientist Is Changing That.
 
Jessica Wade has added nearly 700 Wikipedia biographies for
 important female and minority scientists in less than two 
 years.
 
'''

bloomberg_com = '''
The Space Race: From Apollo 11 to Elon Musk
 
It's 50 years since the world was gripped by historic images
 of Apollo 11, and Neil Armstrong -- the first man to walk 
 on the moon. It was the height of the Cold War, and the charts
 were filled with David Bowie's Space Oddity, and Creedence's 
 Bad Moon Rising. The world is a very different place than 
 it was 5 decades ago. But how has the space race changed since
 the summer of '69? (Source: Bloomberg)
 
 
Twitter CEO Jack Dorsey Gives Talk at Apple Headquarters
 
Twitter and Square Chief Executive Officer Jack Dorsey 
 addressed Apple Inc. employees at the iPhone maker’s headquarters
 Tuesday, a signal of the strong ties between the Silicon Valley giants.
'''

# write your code here
ap = argparse.ArgumentParser()
ap.add_argument('-d', 'dir', nargs='?', help='Directory for tab')
args = ap.parse_args()
_dir_ = args.dir
# abc_com -> var
# abc.com -> url
# abc     -> tab

visited_pages = set()


def url_validate(url):
    """  :param url: Receive url :return: True if url is valid  """
    return url == 'nytimes.com' or url == 'bloomberg.com'


def url_to_var(url):
    """ :param url: url :return: reformat it as a string """
    return url.replace('.', '_')


def var_to_tab(var):
    """
    :param var: receive a var
    :return: split the var '-' and return the first element
    """
    return var.split('_')[0]


def page_visit(var):
    with open(f'{os.path.join(_dir_, var_to_tab(var))}.txt', 'r') as tab:
        visited_pages.add(var_to_tab(var))
        print(eval(var), file=tab)


def show_page_visit(tab):
    with open(f'{os.path.join(_dir_, var_to_tab(tab))}.txt', 'r') as tab:
        print(tab.read())


#########################################################################
if _dir_:
    try:
        os.mkdir(_dir_)
    except FileExistsError:
        pass
while True:
    user_input = input()
    if user_input == 'exit':
        exit(1)
    elif user_input in visited_pages:
        show_page_visit(user_input)
    elif url_to_var(user_input):
        user_input = url_to_var(user_input)
        page_visit(user_input)

        user_input = var_to_tab(user_input)
        show_page_visit(user_input)
    else:
        print('Incorrect URl')
