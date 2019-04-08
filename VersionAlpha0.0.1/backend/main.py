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

#Generate indexes for a list of submissions
#POST format:
# {
#     "ids":"[list of submission ids]"
# }
@app.route('/api/v1/index_submissions', methods=["POST"])
def index_submissions():
    if "ids" in request.form:
        print(request.form)
        submissions = json.loads(request.form["ids"])
        print(submissions)
        for s in submissions:
            #for each file
            for i in indexers:
                #generate an index for each indexer (dont store result of function, index handles that itself)
                job_queue.enqueue(i.index,s,result_ttl=0)

        return "Ok.", 200
    else:
        print("nonono")
        #no submission ids were sent
        print(request.form)
        return "Malformed input.", 400

if __name__ == '__main__':
    app.run(host='0.0.0.0')