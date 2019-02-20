copy config.template.ini to config.ini and configure.
the stuff in tools can help set up a test database until we have a proper one.

start_services.sh : will start the redis docker found in dockerfiles (you may have to do more stuff to set that up) as well as starts the rq worker
requirements.txt  : should have evrything you need in your python environment, in the future we will likely put all of this into a docker to make it easier

databasePostgresSimple.py : is a temporary script and needs to be re-written when we have a proper database. doesn't handle failures well at all.

NOTE TO CODY:
I only converted the non random centroids indexer, as it already had database stuff in it. use diff or somthing simmilar to see the changes I made, they are few and far between. I also dont have a reporting thing yet, it only puts the indexes into the database. The other indexer is labeled as "broken", we can fix it later.

NOTE:
This does not contain any of the test data we are using, contact joey or cody for that