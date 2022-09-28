from datetime import datetime as dt
from time import time

def name_logger(info):
    time = dt.now(). strftime('%H:%M')
    with open('log.csv', 'a') as file:
        file.write('{};name;{}\n'
                    .format(time, info))

def num_logger(info):
    time = dt.now(). strftime('%H:%M')
    with open('log.csv', 'a') as file:
        file.write('{};num;{}\n'
                    .format(time, info))

def text_logger(info):
    time = dt.now(). strftime('%H:%M')
    with open('log.csv', 'a') as file:
        file.write('{};text;{}\n'
                    .format(time, info))
