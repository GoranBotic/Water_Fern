FROM ubuntu
LABEL Description="This image is used to run the Water Fern front-end application."
RUN apt -y update && apt -y upgrade &&  apt -y install curl && apt -y install build-essential 
RUN apt -y install software-properties-common
RUN apt-add-repository -y -r ppa:chris-lea/node.js && curl -sSL https://deb.nodesource.com/gpgkey/nodesource.gpg.key | apt-key add - && VERSION=node_10.x && DISTRO="$(lsb_release -s -c)" && echo "deb https://deb.nodesource.com/$VERSION $DISTRO main" | tee /etc/apt/sources.list.d/nodesource.list && echo "deb-src https://deb.nodesource.com/$VERSION $DISTRO main" | tee -a /etc/apt/sources.list.d/nodesource.list && apt -y update
RUN apt -y install python3 && apt -y install python3-pip && pip3 install flask && pip3 install psycopg2 
RUN apt -y install nodejs 
EXPOSE 5000
COPY package.json /home/waterFern/website/package.json
WORKDIR /home/waterFern/website
RUN npm --silent install 
RUN pip3 install requests
