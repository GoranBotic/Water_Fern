import sys
import json
from flask import Flask, render_template, redirect, request, send_from_directory,jsonify
from zipfile import ZipFile
import os 
import requests

import config
dbm = __import__(config.DATABASE_MANAGER)
manager = dbm.DatabaseManager()

#Start webserver
app = Flask(__name__, static_folder='website/build')

#Test page
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    if path != "" and os.path.exists("website/build/" + path):
        return send_from_directory('website/build', path)
    else:
        return send_from_directory('website/build', 'index.html')

#upload a submission
@app.route('/api/v1/uploadsubmission', methods=['GET','POST'])
def upload_submission():
    print("test")
    fi = request.files['file']
    if "uID" in request.form:
        userID = request.form["uID"] 
    else:
        return "Malformed input.", 400
    if "aID" in request.form:
        assignID = request.form["aID"] 
    else:
        return "Malformed input.", 400


    if fi is not None:
        #TODO: zip parse error detection
        zipf = ZipFile(fi)
        names = zipf.namelist() 
        for name in names:
                dictToSend = dict() 
                dictToSend["ids"] = []
                with zipf.open(name, 'r') as theFile:
                        #TODO: need to detect the language of the file and pass the correct language to put_file
                        theid = manager.put_file(theFile, name, "Java",assignID,userID)
                        dictToSend["ids"].append(theid)
        print(dictToSend)
        idStr = "["
        for i in dictToSend['ids']:
                idStr = idStr + str(i) + "," 
        idStr = idStr[:-1] 
        idStr += "]"
        res = requests.post("http://"+config.BACKEND_ADDRESS+":12345/api/v1/index_submissions", data = {'ids':idStr})
        #print('response from server:',res.text)
        #dictFromServer = res.json()

    return "Ok.", 200
        

#get similar files
@app.route('/api/v1/getassociations', methods=['POST','GET'])
def get_associations():
        if "fID" in request.form:
                fID = request.form["fID"] 
                return jsonify(associations=manager.get_associations(fID))
        else:
                return "Malformed input.", 400

if __name__ == '__main__':
    app.run(host='0.0.0.0')