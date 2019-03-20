FROM ubuntu
LABEL Description="This image is used to run the Water Fern back-end application."
RUN apt -y update && apt -y upgrade && apt -y install python3 && apt -y install python3-pip && pip3 install --upgrade gensim && pip3 install antlr4-python3-runtime && pip3 install flask && pip3 install psycopg2-binary && pip3 install redis && pip3 install rq

RUN apt -y update && apt -y upgrade
RUN apt -y install python3-dev nginx
RUN pip3 install uwsgi

COPY waterfernBackend /etc/nginx/sites-available/waterfernBackend
RUN ln -s /etc/nginx/sites-available/waterfernBackend /etc/nginx/sites-enabled

COPY certificates/cert.pem /home/certificates/cert.pem
copy certificates/key.pem /home/certificates/key.pem

expose 443