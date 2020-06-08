#!/usr/bin/env python3
import sys
import json
from PIL import Image,ImageFont,ImageDraw

"""
This module checks the countries file and draws a map with each player's army
"""

country = sys.argv[1]

with open('countries.json') as f:
    data = json.loads(f.read())[country]

image_file = f'./maps/{country}.png'
font = ImageFont.truetype('arial.ttf', size = 10)

def write_map(x,y,text,color):
    draw = ImageDraw.Draw(img)
    draw.ellipse((x-2,y-2,x+20,y+15),fill=color,outline='white')
    draw.text((x,y),text,font=font,fill='black',outline='white')

img = Image.open(image_file)

for province in data:
    x = int(data[province]['x'])
    y = int(data[province]['y'])
    units = data[province]['units']
    write_map(x,y,units,data[province]['owner'])

img.save('temp_map.png')
img.show()
