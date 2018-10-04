import Image
from CS329E-Project-1 import app
from flask import flask, render_template, request
from flask_upload import upload

filename = app.upload()

def uploadAction():
    if request.method == "POST":
        request.form["upload"]
        display()

def display():
    picture = Image.open(filename)
    picture.show()

