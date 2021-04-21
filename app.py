from flask import Flask, render_template, request, url_for, redirect, session
from google.api_core.datetime_helpers import DatetimeWithNanoseconds
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import firestore
from PIL import Image
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

##FLASK FRAMEWORK
app = Flask(__name__)
app.secret_key = "testing"

@app.route("/")
def main():
    doc_ref = fdb.collection(u'license').document(u''+Uid)
    doc = doc_ref.get()
    if doc.exists:
        documentData=doc.to_dict()
        expireDate=documentData.get('From')
        if expireDate == expireDate:
            color='red'
        else:
            color='red'    

    return render_template('index.html',color=color,result=documentData)

if __name__ == '__main__':
    app.run(debug=True)