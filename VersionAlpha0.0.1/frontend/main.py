import sys
import json
from flask import Flask, render_template, redirect, request
from zipfile import ZipFile

#Start webserver
app = Flask(__name__)

#Test page
@app.route('/')
def index():
    return render_template("index.html")

#upload a submission
@app.route('/api/v1/upload_submission', methods=['POST'])
def upload_submission():
    fi = request.files['file']
    if fi is not None:
        #TODO: zip parse error detection
        zipf = ZipFile(fi)
        


if __name__ == '__main__':
    app.run()