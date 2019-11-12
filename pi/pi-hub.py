import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import time
import requests


# firebase init

cred = credentials.Certificate("./serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

# get data

ref = db.collection(u'devices')
docs = ref.stream()

for doc in docs:
    print(u'{} => {}'.format(doc.id, doc.to_dict()))
