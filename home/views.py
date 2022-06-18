from django.shortcuts import render
import pyrebase

config={
    "apiKey": "AIzaSyDZJfuNtwIe2l5_FZZcHiO0N7fHnovDt_4",
    "authDomain": "test1-ce649.firebaseapp.com",
    "databaseURL": "https://test1-ce649-default-rtdb.firebaseio.com",
    "projectId": "test1-ce649",
    "storageBucket": "test1-ce649.appspot.com",
    "messagingSenderId": "792044520704",
    "appId": "1:792044520704:web:ef4c6d51c2756972859fe5",

}
firebase=pyrebase.initialize_app(config)
authe = firebase.auth()
database=firebase.database()
# Create your views here.
def html(request):
    channel_name = database.child('data').child('name').get().val()
    channel_image = database.child('data').child('image').get().val()
    return render(request,"chat.html",{
     "channel_name":channel_name,
     "channel_image":channel_image
    })