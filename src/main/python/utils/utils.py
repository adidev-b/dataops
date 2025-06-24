import logging
from typing import List, Callable


def logger(appname: str, level: str) -> Callable:
    """
    Importance types can be - debug, info, warning, error, critical
    :param appname:
    :return: base logger function to be used

    """
    applog = logging.getLogger(appname)
    applog.formatter('%(ascxtime)s - %(name)s - %(levelname)s - %(message)s')
    applog.setLevel(f'logging.{level}')

    return applog


def make_pretty(func):
    # define inner function
    def inner():
        print('I got decorated')
        # call original function
        func()
    return inner


# define original function
@make_pretty
def ordinary():
    print('I am ordinary')




