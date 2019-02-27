copy config.template.ini to config.ini and configure.
the stuff in tools can help set up a test database until we have a proper one.

start_services.sh : will start the redis container found in dockerfiles, as well as the backend container found in dockerfiles. The backend container will be running the web-server, as well as an rq-worker, and will open an interactive shell so you can interact with the environment if needed(Hit enter and the messsage from flask will disappear). Note you will need to build the redis container and the backend containers first(with the build.sh scripts). 
    the backend container is currently ~850MB, this is mostly from pip, which I used to install dependencies. The final version of this can be trimmed by a lot, but for now its convenient for the container to have pip, and other expected features.
    
    IMPORTANT
        start_services.sh MUST be run from within the backend directory. IF you want start_services.sh to run properly THEN the current working directory (as reported by pwd) MUST be backend. The backend container simply mounts the current working directory as the main directory in the container, this means that we can modify the back end without having to update the image.


requirements.txt  : should have evrything you need in your python environment, in the future we will likely put all of this into a docker to make it easier

databasePostgresSimple.py : is a temporary script and needs to be re-written when we have a proper database. doesn't handle failures well at all.

NOTE TO CODY:
I only converted the non random centroids indexer, as it already had database stuff in it. use diff or somthing simmilar to see the changes I made, they are few and far between. I also dont have a reporting thing yet, it only puts the indexes into the database. The other indexer is labeled as "broken", we can fix it later.

NOTE:
This does not contain any of the test data we are using, contact joey or cody for that