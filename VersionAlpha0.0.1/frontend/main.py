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
app = Flask(__name__, static_folder='templates/', static_url_path="/templates/")
app.config['APPLICATION_ROOT'] = "templates/"

#Test page
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    if path != "" and os.path.exists("templates/" + path):
        return send_from_directory('templates/', path)
    else:
        return send_from_directory('templates/', 'home.html')

#upload a submission
@app.route('/api/v1/uploadsubmission', methods=['GET','POST'])
def upload_submission():
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
@app.route('/api/v1/getAssociations', methods=['GET','POST'])
def get_associations():
        if "fID" in request.form:
            print("getting associations")
            fID = request.form["fID"] 
            ret = manager.get_associations(fID)
            print(ret)
            return jsonify(ret)
        else:
                return "Malformed input.", 400

#get list of offerings for a class
@app.route('/api/v1/getClassList', methods=['GET','POST'])
def get_classes():
    thing = manager.get_class_list()
    ret = jsonify(thing)
    return ret

#get list of offerings for a class
@app.route('/api/v1/getOfferingList', methods=['GET','POST'])
def get_offerings():
    if "classID" in request.form:
        oID = request.form["classID"] 
        thing = manager.get_offering_list(oID)
        ret = jsonify(thing)
        return ret
    else:
        return "Malformed input.", 400

#get list of assignments for an offering
@app.route('/api/v1/getAssignmentList', methods=['GET','POST'])
def get_assignments():
    if "offeringID" in request.form:
        oID = request.form["offeringID"] 
        thing = manager.get_assignment_list(oID)
        ret = jsonify(thing)
        return ret
    else:
        return "Malformed input.", 400

#get list of assignments for an offering
@app.route('/api/v1/getSubmissionsList', methods=['GET','POST'])
def get_submissions():
    print(request.form)
    if "assignmentID" in request.form:
        aID = request.form["assignmentID"] 
        thing = manager.get_submissions_for(aID)
        print("here")
        print(thing)
        ret = jsonify(thing)
        return ret
    else:
        print("failed")
        return "Malformed input.", 400

#get list of assignments for an offering
@app.route('/api/v1/getSubmission', methods=['GET','POST'])
def get_submission():
    print(request.form)
    if "submissionID" in request.form:
        sID = request.form["submissionID"] 
        thing = manager.get_file(sID)
        ret = [thing[0], bytes(thing[1]).decode(), thing[2]]
        ret = jsonify(ret)
        return ret
    else:
        print("failed")
        return "Malformed input.", 400

if __name__ == '__main__':
    app.run(host='0.0.0.0')