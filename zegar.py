import datetime
import requests
import time
from neopixel import *
import argparse
from ColourDict import losowyKolor,colour
from LampkiDict import slownikLampek
import random


def wypiszGodz(strip, i):
    for i, v in enumerate(i[::-1]):
        if v == '1':
            strip.setPixelColor(slownikLampek['F'] - i, colour['blue'])


def wypiszMin(strip, i):
    for i, v in enumerate(i[::-1]):
        if v == '1':
            strip.setPixelColor(slownikLampek['N'] + i, colour['gold'])

def wypiszSec(strip, i):
    for i, v in enumerate(i[::-1]):
        if v == '1':
            strip.setPixelColor(slownikLampek['T'] - i, colour['royalblue'])

def wypiszDzien(strip, i):
    for i, v in enumerate(i[::-1]):
        if v == '1':
            strip.setPixelColor(slownikLampek['?'] + i, colour['forestgreen'])

def ZegarBinarny(strip):
    now = datetime.datetime.now()
    day = now.day
    hour = now.hour+1
    min = now.minute
    sec = now.second
    hour = "{0:b}".format(hour)
    min = "{0:b}".format(min)
    sec = "{0:b}".format(sec)
    day = "{0:b}".format(day)
    wypiszDzien(strip,day)
    wypiszGodz(strip,hour)
    wypiszMin(strip,min)
    wypiszSec(strip,sec)
    strip.show()





