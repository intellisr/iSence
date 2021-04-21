import serial
import time
import string
import pynmea2
from google.api_core.datetime_helpers import DatetimeWithNanoseconds
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import firestore
import pytz     

# Fetch the service account key JSON file contents
cred = credentials.Certificate('isence-firebase-adminsdk-r320k-7a2dce5241.json')
# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://isence-default-rtdb.firebaseio.com/'
})

utc=pytz.UTC
fdb = firestore.client()
Uid = 'CAX7124'

doc_ref = fdb.collection(u'license').document(u''+Uid)

doc = doc_ref.get()
if doc.exists:
	documentData=doc.to_dict()
	expireDate=documentData.get('From')
	if expireDate == expireDate:
		while True:
			port="/dev/ttyAMA0"
			ser=serial.Serial(port, baudrate=9600, timeout=0.5)
			dataout = pynmea2.NMEAStreamReader()
			newdata=ser.readline()

			if newdata[0:6] == "$GPRMC":
				newmsg=pynmea2.parse(newdata)
				lat=newmsg.latitude
				lng=newmsg.longitude
				ref2 = db.reference('Location/'+ Uid)
				ref2.update(newmsg)
				gps = "Latitude=" + str(lat) + "and Longitude=" + str(lng)
				print(gps)
else:
    print(u'No such document!')

