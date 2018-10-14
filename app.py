from flask import Flask, render_template, request, redirect, url_for, send_file, send_from_directory
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
        file.save(os.path.join('static', 'picture.jpg'))
        return redirect(url_for('index'))
    return render_template("upload.html")


@app.route("/edit", methods=['POST', 'GET'])
def edit():
    return render_template("edit.html")


@app.route("/edit-2", methods=["POST"])
def edit2():
    print(request.form['height'])
    print(request.form['width'])
    try:
        height = int(request.form['height'])
        width = int(request.form['width'])
        size = width, height
        picture = Image.open('static/picture.jpg')
        picture = picture.resize((width, height), Image.ANTIALIAS)
        picture.save('static/picture.jpg')
    except ValueError:
        print("Error found.")
        pass
    return render_template("edit.html")


@app.route("/display")
def display():
    uploadAction('static/picture.jpg')
    return redirect(url_for('edit'))


@app.route('/download', methods=['GET', 'POST'])
def download():
    uploads = os.path.join(app.root_path, app.config[])
    return send_from_directory(directory=uploads, filename='picture.jpg')

@app.route("/addText", methods=['POST'])
def addText():
    if request.method == 'POST':
        text = request.form['text']
    # Open image
        img = Image.open(filename)

    # Add text to image

    # Save image

    # Display image
    #return

def setFileName(name):
    global filename
    filename = name


def uploadAction(name):
    picture = Image.open(name)
    picture.show()
    return


def getFileName():
    return filename


def returnSuccess():
    return "success"


if __name__ == '__main__':
    app.run()
