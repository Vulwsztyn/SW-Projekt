import datetime
import requests
import time
from neopixel import *
import argparse
from ColourDict import losowyKolor
from LampkiDict import slownikLampek
import random


def wypiszSec(strip, i):
    for i, v in enumerate(i):
        if v == '1':
            strip.setPixelColor(slownikLampek['F'] - i, losowyKolor())


def wypiszMin(strip, i):
    for i, v in enumerate(i):
        if v == '1':
            strip.setPixelColor(slownikLampek['N']+ 1 + i, losowyKolor())

def wypiszGodz(strip, i):
    for i, v in enumerate(i):
        if v == '1':
            strip.setPixelColor(slownikLampek['T'] - i, losowyKolor())

def wypiszDzien(strip, i):
    for i, v in enumerate(i):
        if v == '1':
            strip.setPixelColor(slownikLampek['?'] + i, losowyKolor())


def ZegarBinarny(strip):
    now = datetime.datetime.now()
    day = now.day
    hour = now.hour
    min = now.minute
    sec = now.second
    hour = "{0:b}".format(hour)
    min = "{0:b}".format(min)
    sec = "{0:b}".format(sec)
    day = "{0:b}".format(day)
    wypiszDzien(day)
    wypiszGodz(hour)
    wypiszMin(min)
    wypiszSec(sec)
    strip.show()

