FROM ubuntu
LABEL Description="This image is used to run the Water Fern front-end application."
RUN apt -y update && apt -y upgrade &&  apt -y install curl && apt -y install build-essential 
#RUN apt -y install software-properties-common
RUN apt -y install python3 && apt -y install python3-pip && pip3 install flask && pip3 install psycopg2-binary 
RUN pip3 install requests
RUN apt -y update && apt -y upgrade
RUN apt -y install python3-dev nginx
RUN pip3 install uwsgi

COPY waterfernFrontend /etc/nginx/sites-available/waterfernFrontend
RUN ln -s /etc/nginx/sites-available/waterfernFrontend /etc/nginx/sites-enabled

COPY certificates/cert.pem /home/certificates/cert.pem
copy certificates/key.pem /home/certificates/key.pem

RUN pip3 install flask-login

EXPOSE 80
expose 443
