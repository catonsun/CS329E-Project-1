from flask import Flask, render_template, request, redirect, url_for
import os
import tkinter as tk
from PIL import Image, ImageTk
app = Flask(__name__)


@app.route("/")
def index():
    return render_template("home.html")


@app.route("/upload", methods=['POST', 'GET'])
def upload():
    if request.method == 'POST':
        file = request.files['file']
        filename = file.filename
        file.save(os.path.join('UPLOAD_FOLDER', filename))
        uploadAction(file)
        return redirect(url_for('index'))
    return render_template("upload.html")

def uploadAction(filename):
    picture = Image.open(filename)
    picture.show()
    return

if __name__ == '__main__':
    app.run()
