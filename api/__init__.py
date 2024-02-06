from flask import Flask
import firebase_admin
from firebase_admin import credentials
import pyrebase

firebase_client_config = {
    "apiKey": "AIzaSyB5oYH_7CMXhDwPdMudUlhpNWrjmADxX6o",
    "authDomain": "gram-d45eb.firebaseapp.com",
    "databaseURL": "https://gram-d45eb-default-rtdb.europe-west1.firebasedatabase.app",
    "projectId": "gram-d45eb",
    "storageBucket": "gram-d45eb.appspot.com",
    "messagingSenderId": "503701848987",
    "appId": "1:503701848987:web:2d97d058966bddc920973e"
}

cred = credentials.Certificate("credentials.json")

# Check if Firebase app is already initialized
if not firebase_admin._apps:
    firebase = firebase_admin.initialize_app(cred)

# Initialize Firebase client
pb = pyrebase.initialize_app(firebase_client_config)

auth_client = pb.auth()

db = pb.database()

app = Flask(__name__)

app.secret_key = "ea9873ab493d0c43d24d89ee1f96080b91521d3c6ae0e0199a673ffef92e2021" #GRAM sha256 hash


from api import endpoints



