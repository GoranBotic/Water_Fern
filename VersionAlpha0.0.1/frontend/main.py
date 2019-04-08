import sys
import json
from flask import Flask, render_template, redirect, request, send_from_directory,jsonify
from zipfile import ZipFile
import os 
import requests
import time

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
    if "file" in request.files:
        fi = request.files['file']
    else:
        return "Malformed input.", 400
    if "aID" in request.form:
        assignID = request.form["aID"] 
    else:
        return "Malformed input.", 400
    bulkUpload = False 
    if "bulkUpload" in request.form:
        bulkUpload = bool(request.form["bulkUpload"])
    
    if not bulkUpload:
        if "uID" in request.form:
            userID = request.form["uID"] 
        else:
            return "Malformed input.", 400


    if fi is not None:
        try:
            zipf = ZipFile(fi)
            names = zipf.namelist() 

            #this dictionary defines the data to be posted to the backend server
            dictToSend = dict() 
            dictToSend["ids"] = []
            dictToSend["lang"] = [] 

            failedToSubmit = [] 

            for name in names:
                extensionStart = name.rfind(".") 
                if extensionStart == -1:
                    continue 

                extension = name[extensionStart+1:].lower()

                lang = None
                if extension in config.JAVA_EXTENSIONS:
                    lang = "Java"
                if extension in config.CPP_EXTENSIONS:
                    lang = "cpp" 
                if extension in config.C_EXTENSIONS:
                    lang = "c" 

                
                if lang == None:
                    failedToSubmit.append(name)
                    continue 
                
                if bulkUpload:
                    userID = None
                    uIDStop = name.find("/")
                    #TODO: extract the userame from the top level folder 
                    #When the bulk upload flag is set, the sytem will assume that a zip file containing folders is sent 
                    #each folder is assumed to be named according to the user name of the user who submit the assignment in that folder 
                    #everying under the top folder is considered to be the submission 
                    #ex cd15oy <- a folder in the zip file VV contents
                    #       src 
                    #           file1
                    #           file2
                    #       tests
                    #           file1
                    #           file2
                    #we need to check that the user actually exists
                    #if not, we need to warn the user, however, we should still process the other folders
                    #if one student screws up the formatting, it should not stop the entire bulk submission 
                    if uIDStop == -1:
                        failedToSubmit.append(name) 
                        continue
                    else:
                        userID = manager.look_up_user_ID(name[:uIDStop],True) #get the user id, or make one if it is missing
                        

                with zipf.open(name, 'r') as theFile: 
                    nameStart = name.rfind("/")
                    name = name[nameStart+1:]
                    theid = manager.put_file(theFile, name, lang, assignID, userID)

                    dictToSend["ids"].append(theid)

            
            idStr = "["
            for i in dictToSend['ids']:
                idStr = idStr + str(i) + "," 
            idStr = idStr[:-1] 
            idStr += "]"
            print("poke")
            print(dictToSend)
            print(names)

            #TODO:once we have an actual unchanging address we need to change verify=False to verify=/path/to/public/cert
            #A certificate is only valid on a specific address, and as of right now all our components are using the computers assigned IP, not local host, this means that when we host things externally we should skip some problems 
            # it also means that in order to verify the backend certificate, we would need to remake a certficate every time the laptops IP changes, so for now we use verify=False  
            res = requests.post("https://"+config.BACKEND_ADDRESS+":12345/api/v1/index_submissions", data = {'ids':idStr}, verify=False)
            
            #TODO: this needs to redirect the user, and it should explain any issues which came up 
            if len(failedToSubmit) > 0:
                return "Failed to submit: " + str(failedToSubmit), 200
            else:
                # time.sleep(10)
                return redirect("/home.html", code=302)#str(manager.find_progress(dictToSend["ids"]))#

        except Exception as e:
            print(e)
            return "Invalid Zip Archive", 400
        
#upload submissions in bulk
@app.route('/api/v1/uploadBulkSubmissions', methods=['GET','POST'])
def upload_bulk_submissions():
    pass

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

#get submissions to assignment
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