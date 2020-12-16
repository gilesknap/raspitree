#!/usr/bin/env python3

import argparse
from tree import RGBXmasTree
from time import sleep
from colorzero import Color, Hue

tree = RGBXmasTree()

tree.color = Color("red")

parser = argparse.ArgumentParser()
parser.add_argument(
    "brightness", help="brightness for all LEDs", type=float, default=0.1, nargs="?"
)
parser.add_argument(
    "degrees",
    help="degrees of hue separation between steps",
    type=int,
    default=25,
    nargs="?",
)
args = parser.parse_args()

tree.brightness = args.brightness

try:
    while True:
        for count in range(32):
            for n, pixel in enumerate(tree):
                hue = Hue(deg=args.degrees * n)
                pixel.color += hue
                print(f"pixel:{n} \t count:{count} \t Hue:{hue:.2f}")
        tree.brightness = args.brightness
except KeyboardInterrupt:
    tree.close()
    tree = RGBXmasTree()
    tree.close()
