from flask import Flask, render_template, request, redirect, url_for
import os
import tkinter as tk
from PIL import Image, ImageTk
app = Flask(__name__)


filename = ""


@app.route("/")
def index():
    if filename == "":
        return render_template("home.html")
    else:
        return render_template("home2.html")


@app.route("/upload", methods=['POST', 'GET'])
def upload():
    if request.method == 'POST':
        file = request.files['file']
        filename = file.filename
        setFileName(filename)
        file.save(os.path.join('static', 'picture'))
        uploadAction(file)
        return redirect(url_for('index'))
    return render_template("upload.html")


@app.route("/edit", methods=['POST', 'GET'])
def edit():
    return render_template("edit.html", picture_name=filename)


def setFileName(name):
    global filename
    filename = name


def uploadAction(filename):
    picture = Image.open(filename)
    picture.show()
    return


def getFileName():
    return filename


def returnSuccess():
    return "success"


if __name__ == '__main__':
    app.run()
