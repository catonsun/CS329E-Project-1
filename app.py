from flask import Flask, render_template, request, redirect, url_for
import os
from PIL import Image

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def upload():
    if request.method == 'POST':
        file = request.files['file']
        filename = file.filename
        imagePath = os.path.join('uploadFolder', filename)
        file.save(imagePath)

        uploadAction(imagePath)

    return render_template("upload.html")

@app.route('/upload', methods=['POST'])
def chooseFile():
    if request.method == 'POST':
        file = request.files['file']
        filename = file.filename
        imagePath = os.path.join('uploadFolder', filename)
        file.save(imagePath)

        uploadAction(imagePath)

    return

def uploadAction(filename):
    #if request.method == "POST":
    #    request.form["upload"]
    #    display()
    picture = Image.open(filename)
    picture.show()
    return
if __name__ == '__main__':
    app.run()
