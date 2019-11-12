import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

from sense_hat import SenseHat

import time
import requests

# firebase init

cred = credentials.Certificate("./serviceAccountKey.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

# get data

ref = db.collection(u'devices')
def get_document_by_name(name):
  doc = ref.document(name).get()
  return doc.to_dict()

sense = SenseHat()

r = (255, 0, 0)         # red
g = (0,255,0)           # green
b = (0,0,255)           # blue
y = (255,255,0)         # yellow
w = (255,255,255)       # white
O = (0, 0, 0)           # disabled

red = (255, 0, 0)       # red
green = (0,255,0)       # green
blue = (0,0,255)        # blue
yellow = (255,255,0)    # yellow
blue_dark = (0,0,63)    # blue
yellow_dark = (63,63,0) # yellow
white = (255,255,255)   # white
black = (0, 0, 0)       # disabled

defaultDeviceSettings = [
O, O, y, O, O, y, O, O,
O, O, O, O, O, O, O, O,
O, O, O, O, O, O, O, O,
b, O, O, O, O, O, O, b,
O, O, y, O, O, y, O, O,
r, O, O, O, O, O, O, r,
r, O, O, O, O, O, O, r,
r, O, O, b, b, O, O, r,
]

# postions on matrix

doors = [[(0,5),(0,6),(0,7)], [(7,5),(7,6),(7,7)]]
lights = [(2,0),(5,0),(2,4),(5,4)]
plugs = [(0,3), (7,3),(3,7),(4,7)]

sense.set_pixels(defaultDeviceSettings)

lightSettings = get_document_by_name('lights')
plugSettings = get_document_by_name('plugs')
doorSettings = get_document_by_name('doors')

for setting in lightSettings.keys():
  if(lightSettings[setting] == True):
    sense.set_pixel(lights[int(setting)][0],  lights[int(setting)][1], yellow)
  else:
    sense.set_pixel(lights[int(setting)][0],  lights[int(setting)][1], yellow_dark)

for setting in plugSettings.keys():
  if(plugSettings[setting] == True):
    sense.set_pixel(plugs[int(setting)][0],  plugs[int(setting)][1], blue)
  else:
    sense.set_pixel(plugs[int(setting)][0],  plugs[int(setting)][1], blue_dark)

for setting in doorSettings.keys():
  if(doorSettings[setting] == True):
    for pixel in doors[int(setting)]:
      sense.set_pixel(pixel[0],  pixel[1], green)
  else:
    for pixel in doors[int(setting)]:
      sense.set_pixel(pixel[0],  pixel[1], red)