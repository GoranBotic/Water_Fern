import sys
import json
from flask import Flask, render_template, redirect, request, send_from_directory,jsonify, flash, session
from flask_login import LoginManager, login_user, login_required, current_user, UserMixin, logout_user
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

#Set the secret key for session management 
app.secret_key = b'aldj3kl2j59f90idD^$%DSF#&$)sdkl234ip0s9d#%#$#$'

@app.before_request 
def make_session_permanent():
    session.permanent = True

#Initialize a login_manager 
login_manager = LoginManager()
login_manager.login_view = "/api/v1/login"
login_manager.init_app(app)
login_manager.session_protection = "strong"


#define a class for users 
class User(UserMixin):
    pass 

#This is cheesy, but its all we need
#TODO: periodically check this dict for dead users to prune 
loggedInUsers = dict() 
    
@login_manager.user_loader
def load_user(id):
    print(id)
    print("load user")
    #If we get to this point then flask has already verified that the sessionID is valid, and has not expired
    #so we just grab the user from out collection of logged in users 
    if id in loggedInUsers:
        return loggedInUsers[id]
    else:
        return None 

#validates credentials and logs users in 
@app.route('/api/v1/login', methods=['GET', 'POST'])
def login():
    if "uID" in request.form and "pWord" in request.form:
        
        user = User() 
        uID = request.form["uID"]
        user.id = uID
        pWord = request.form["pWord"]
        
        #check credentials 
        validCredentials = manager.validateUser(uID, pWord)
        if len(validCredentials) > 0:
            if len(validCredentials[0]) > 0:
                if validCredentials[0][0]:
                    global loggedInUsers 
                    print("the uID is: " + uID)
                
                    loggedInUsers[uID] = user
                    login_user(user, remember = True)
                
                    return redirect("/home.html", code=302)

    return send_from_directory('templates/', 'login.html')

#logs users out 
@app.route("/api/v1/logout")
@login_required
def logout():
    loggedInUsers[current_user.id] = None 
    logout_user()
    return redirect("/api/v1/login", code=302)

#Retrives pages from the website root
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
@login_required
def serve(path):
    if path != "" and os.path.exists("templates/" + path):
        return send_from_directory('templates/', path)
    else:
        return send_from_directory('templates/', 'home.html')

#Retrives pages from the website root
@app.route('/api/v1/god', methods=['GET', 'POST'])
@login_required
def god():
    if current_user.get_id() == "Paetric":
        if "uID" in request.form and "pWord" in request.form:
            uID = request.form["uID"] 
            pWord = request.form["pWord"] 
            manager.addUser(uID, pWord) 
            return redirect("/api/v1/god", code=302)
        else:
            return "<form action='/api/v1/god' method='POST'> \
                    User ID: <input type='textbox' name='uID' placeholder='ab14st'/> \
                    <br> \
                    <br> \
                    Password: <input type='textbox' name='pWord' placeholder='******'/> \
                    <br> \
                    <br> \
                    <input type='submit' value='Submit'/>\
                    </form>", 200

    else:
        return redirect("/home.html", code=302)



#upload a submission
@app.route('/api/v1/uploadsubmission', methods=['POST'])
@login_required
def upload_submission():
    if "file" in request.files:
        fi = request.files['file']
    else:
        return "Malformed input.", 400
    if "aID" in request.form:
        assignID = request.form["aID"] 
    else:
        return "Malformed input.", 400
    print(assignID)
    bulkUpload = True#False 
    if "bulkUpload" in request.form:
        if request.form["bulkUpload"] == "True":
            bulkUpload = True 
 
    
    userID = None 
    if not bulkUpload:
        if "uID" in request.form:
            userID = request.form["uID"] 
        else:
            return "Malformed input.", 400

    if fi is not None:
        try:
            zipf = ZipFile(fi)
            names = zipf.namelist() 
        except Exception as e:
            print(e)
            return "Invalid Zip Archive", 400

        #this dictionary defines the data to be posted to the backend server
        dictToSend = dict() 
        dictToSend["ids"] = []
        dictToSend["lang"] = [] 

        failedToSubmit = [] 

        for name in names:
            try:
                extensionStart = name.rfind(".") 
                if extensionStart == -1:
                    continue 

                extension = name[extensionStart+1:].lower()

                lang = None
                if extension in config.JAVA_EXTENSIONS:
                    lang = "Java"
                if extension in config.CPP_EXTENSIONS:
                    lang = "CPP" 
                if extension in config.C_EXTENSIONS:
                    lang = "C" 

                    
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

            except Exception as e:
                print(e)
                print("Error on " + name)
                failedToSubmit.append(name)
            
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

        if len(dictToSend["ids"]) > 0:
            res = requests.post("https://"+config.BACKEND_ADDRESS+":12345/api/v1/index_submissions", data = {'ids':idStr}, verify=False)
            
        #TODO: this needs to redirect the user, and it should explain any issues which came up 
        if len(failedToSubmit) > 0:
            didSubmit = [] 
            for name in names:
                if not (name in failedToSubmit):
                    didSubmit.append(name) 
            ret = "" 
            ret += "<a href='https://0.0.0.0:8001'> Click here to go home </a> <br>" 
            ret += "Navigate to the assignment page to see the analyzed files.\n"
            ret += "Some files were not processed. A list of which files were processed and which were not follows.<br><br><br>" 
            ret += "These files were submit successfully: <br>" + str(didSubmit) + "<br><br>" 
            ret += "These files were ignored: <br>" + str(failedToSubmit) + "<br><br>"

            return ret, 200
        else:

            return redirect("/progressBar.html", code=302)#str(manager.find_progress(dictToSend["ids"]))#


      
        
#get the progress of an indexing
@app.route('/api/v1/getProgress', methods=['POST'])
@login_required
def get_progress():
    if "assignmentID" in request.form:
        assid = request.form["assignmentID"]
        res = manager.find_progress(assid)
        print("poke")
        print(res)
        return str(res)
    else:
        return "Malformed input.", 400

#get similar files
@app.route('/api/v1/getAssociations', methods=['POST'])
@login_required
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
@app.route('/api/v1/getClassList', methods=['POST'])
@login_required
def get_classes():
    thing = manager.get_class_list()
    ret = jsonify(thing)
    return ret

#get list of offerings for a class
@app.route('/api/v1/getOfferingList', methods=['POST'])
@login_required
def get_offerings():
    if "classID" in request.form:
        oID = request.form["classID"] 
        uID = manager.look_up_user_ID(current_user.get_id(), False)
        thing = manager.get_offering_list(oID, uID)
        ret = jsonify(thing)
        return ret
    else:
        return "Malformed input.", 400

#get list of assignments for an offering
@app.route('/api/v1/getAssignmentList', methods=['POST'])
@login_required
def get_assignments():
    if "offeringID" in request.form:
        oID = request.form["offeringID"] 
        thing = manager.get_assignment_list(oID)
        ret = jsonify(thing)
        return ret
    else:
        return "Malformed input.", 400

#get submissions to assignment
@app.route('/api/v1/getSubmissionsList', methods=['POST'])
@login_required
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

#get submissions to assignment ordered by similarity to a document
@app.route('/api/v1/getSubmissionsSimilarTo', methods=['POST'])
@login_required
def get_submissions_similar_to():
    print("getting similar to")
    print(request.form)
    if "assignmentID" in request.form and "docID" in request.form:
        aID = request.form["assignmentID"] 
        sID = request.form["docID"]
        thing = manager.get_submissions_similar_to(aID, sID)
        print("here")
        print(thing)
        ret = jsonify(thing)
        return ret
    else:
        print("failed")
        return "Malformed input.", 400

#get list of assignments for an offering
@app.route('/api/v1/getSubmission', methods=['POST'])
@login_required
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

#add a new class
@app.route('/api/v1/makeClass', methods=['POST'])
@login_required
def make_class():
    print(request.form)
    if "className" in request.form:
        cID = request.form["className"] 
        thing = manager.make_class(cID)

        if thing:
            return redirect("/home.html", code=302)
        else:
            return "Class failed to be added, possibly already exists?", 400
    else:
        print("failed")
        return "Malformed input.", 400

#add a new offering
@app.route('/api/v1/makeOffering', methods=['POST'])
@login_required
def make_offering():
    print(request.form)
    if "cid" in request.form:
        cID = request.form["cid"] 
        thing = manager.make_offering(cID)

        if thing != None :
            if manager.own_offering(thing, manager.look_up_user_ID(current_user.get_id(), False)):
                return redirect("/offeringPage.html", code=302)
            else:
                "Failed to take ownership of offering.", 400
        else:
            return "Offering failed to be added, possibly already exists?", 400
    else:
        print("failed")
        return "Malformed input.", 400

#add a new assignment
@app.route('/api/v1/makeAssignment', methods=['POST'])
@login_required
def make_assignment():
    print(request.form)
    if "oid" in request.form:
        oID = request.form["oid"] 
        thing = manager.make_assignment(oID)

        if thing:
            return redirect("/assignmentPage.html", code=302)
        else:
            return "Assignment failed to be added, possibly already exists?", 400
    else:
        print("failed")
        return "Malformed input.", 400



if __name__ == '__main__':
    app.run(host='0.0.0.0')