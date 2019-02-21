FROM ubuntu
LABEL Description="This image is used to run the Water Fern back-end application."
RUN apt -y update && apt -y upgrade && apt -y install python3 && apt -y install python3-pip && pip3 install --upgrade gensim && pip3 install antlr4-python3-runtime && pip3 install flask && pip3 install psycopg2 && pip3 install redis && pip3 install rq