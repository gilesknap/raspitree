import argparse
from tree import RGBXmasTree
from colorzero import Color


tree = RGBXmasTree(auto_update=False)

bottom_row =    [0 ,6 , 19, 24, 6 ,12, 15, 16, 7]
middle_row=     [1 ,5 , 20, 23, 5 ,11, 14, 17, 8]
top_row=        [2 ,4 , 21, 22, 4 ,10, 13, 18, 9]
star=[3]

order = [bottom_row, middle_row, top_row, star]

parser = argparse.ArgumentParser()
parser.add_argument(
    "brightness", help="brightness for all LEDs", type=float, default=0.1, nargs="?"
)
parser.add_argument(
    "degrees",
    help="degrees of hue separation between steps",
    type=int,
    default=80,
    nargs="?",
)
args = parser.parse_args()

tree.brightness = args.brightness
tree.on()

hue = 0

while True:
    for row in order:
        hue += (args.degrees / 360)
        hue %= 1.0
        for pixel_number in row: 
            c = Color.from_hsv(hue, 1.0, 1.0)
            tree[pixel_number].color = c
    tree.update()
    tree.brightness = args.brightness

