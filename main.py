#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import requests
import time
from neopixel import *
import argparse
from ColourDict import losowyKolor
from LampkiDict import slownikLampek
import random
listaZnakow = "QWERTYUIOPASDFGHJKLZXCVBNM!@#?ĄĘŚŁŻŹĆÓ"


# LED strip configuration:
LED_COUNT = 50  # Number of LED pixels.
# LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
LED_PIN = 10  # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA = 10  # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 10  # Set to 0 for darkest and 255 for brightest
LED_INVERT = False  # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL = 0  # set to '1' for GPIOs 13, 19, 41, 45 or 53


def clear(strip):
    color = Color(0, 0, 0)
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
    strip.show

def zapalPojedyncze(strip, i):
    strip.setPixelColor(i, losowyKolor())
    strip.show()
    strip.setPixelColor(i, Color(0,0,0))


def wyswietlLitere(strip,litera):
    czas = 1
    if litera == " ":
        time.sleep(czas)
        return
    if litera == ".":
        time.sleep(czas * 2)
        return
    if litera in listaZnakow:
        zapalPojedyncze(strip,slownikLampek[litera])
        time.sleep(czas)


def wyswietlTekst(strip,text):
    for i in text.upper():
        wyswietlLitere(strip,i)
    strip.show()


def getFromWebsite():
    response = requests.get('http://amostowski.pl/sw/get.php')
    # print(response.status_code)
    # print(response.content)
    content = str(response.content)
    numer = content[2:content.find(' ')]
    tekst = content[content.find(' ') + 1:len(content) - 5]
    return int(numer), tekst


def postToWebsite(i):
    url = 'http://amostowski.pl/sw/mark.php'
    payload = {'numer': i}
    r = requests.post(url, data=payload)


if __name__ == "__main__":
    # Process arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--clear', action='store_true', help='clear the display on exit')
    args = parser.parse_args()

    # Create NeoPixel object with appropriate configuration.
    strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
    # Intialize the library (must be called once before other functions).
    strip.begin()
    wyswietlTekst("adolf")