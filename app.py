from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def upload():
    if request.method == 'POST':
        file = request.files['file']
        filename = file.filename
        file.save(os.path.join('UPLOAD_FOLDER', filename))
        return redirect(url_for('index'))
    return render_template("home.html")


if __name__ == '__main__':
    app.run()
