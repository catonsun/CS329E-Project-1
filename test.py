import unittest

from flask import Flask, render_template, request, redirect, url_for
import os
import tkinter as tk
from PIL import Image, ImageTk
test = Flask(__name__)


@test.route("/")
def index():
    return render_template("home.html")


@test.route("/upload", methods=['POST', 'GET'])
def upload():
    if request.method == 'POST':
        file = request.files['file']
        filename = file.filename
        return filename
        return redirect(url_for('index'))
    return render_template("upload.html")

def documentType():
    docType = filename[-3:]
    return docType

class Mytest(unittest.TestCase):
    def isCorrectDocumentTypeLower(self):
        self.assertEqual(docType.lower(), "jpg")

    def isCorrectDocumentTypeUpper(self):
        self.assertEqual(docType.upper(), "JPG")

if __name__ == '__main__':
    test.run()