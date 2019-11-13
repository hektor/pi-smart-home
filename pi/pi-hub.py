import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

from sense_hat import SenseHat

import time
import requests

# sensehat init

sense = SenseHat()

# firebase init

cred = credentials.Certificate("./serviceAccountKey.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

# get data

ref = db.collection('devices')
def get_document_by_name(name):
  doc = ref.document(name).get()
  return doc.to_dict()

# sensehat constants

## colors
red = (255, 0, 0)       # red
green = (0,255,0)       # green
blue = (0,0,255)        # blue
yellow = (255,255,0)    # yellow
blue_dark = (0,0,63)    # blue
yellow_dark = (63,63,0) # yellow
white = (255,255,255)   # white
black = (0, 0, 0)       # disabled

## device postions
doors = [[(0,5),(0,6),(0,7)], [(7,5),(7,6),(7,7)]]
lights = [(2,0),(5,0),(2,4),(5,4)]
plugs = [(0,3), (7,3),(3,7),(4,7)]


# add senshat sensor data to database

def set_sensor_settings():
  ref.document('sensors').set({
      'temperature': sense.temp,
      'humidity': sense.humidity
  })

# matrix alarm 

def raise_alarm():
  for door in doors:
    for pixel in door:
      sense.set_pixel(pixel[0],  pixel[1], green)
    for light in lights:
      sense.set_pixel(light[0], light[1], yellow)
    time.sleep(1)
    for light in lights:
      sense.set_pixel(light[0], light[1], black)
    time.sleep(1)
    check_alarm_sensor()

def check_alarm_sensor():
  if get_document_by_name('sensors')['breach']: raise_alarm()

while True:

  check_alarm_sensor()
  
  ## get firestore settings

  lightSettings = get_document_by_name('lights')
  plugSettings = get_document_by_name('plugs')
  doorSettings = get_document_by_name('doors')

  print(lightSettings, plugSettings, doorSettings)

  ## display settings on matrix

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

  time.sleep(1)