import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://faceattendancerealtime-c3cc2-default-rtdb.firebaseio.com/"
})

ref = db.reference('students')

data = {
    "638133": {
        "name": "Yuvaraj",
        "major": "computer science",
        "starting_year": 2022,
        "total_attendance": 22,
        "standing": "G",
        "year": 2,
        "last_attendance_time": '2024-02-08 02:02:54',
    }
}

for key, value in data.items():  # Corrected spelling of 'data'
    ref.child(key).set(value)  # Set the value for each child key
