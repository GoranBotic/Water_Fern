import sys
import json
from flask import Flask, render_template, redirect, request
from redis import Redis
from rq import Queue

#Create job queue
redis_connection = Redis(host="redis_server")
job_queue = Queue(connection=redis_connection)

#Start webserver
app = Flask(__name__)

#Load indexers
import indexers as ind
indexers = []
for i in ind.__all__:
    __import__("indexers."+i)
    indexers.append(sys.modules["indexers."+i])

#Test page
@app.route('/')
def index():
    return render_template("index.html")

#Generate indexes for a list of submissions
#POST format:
# {
#     "ids":"[list of submission ids]"
# }
@app.route('/api/v1/index_submissions', methods=["POST"])
def index_submissions():
    if "ids" in request.form:
        submissions = json.loads(request.form["ids"])
        for s in submissions:
            #for each file
            for i in indexers:
                #generate an index for each indexer (dont store result of function, index handles that itself)
                job_queue.enqueue(i.index,s,result_ttl=0)

        return "Ok.", 200
    else:
        #no submission ids were sent
        return "Malformed input.", 400

if __name__ == '__main__':
    app.run()