docker kill waterfern-postgres 
docker rm waterfern-postgres 
docker kill waterfern-frontend
docker rm waterfern-frontend

docker run -d -p5432:5432 --volume settings:/etc/postgresql --volume logs:/var/log/postgresql --volume data:/var/lib/postgresql --name waterfern-postgres psql-server
sleep 1 
docker run -it --mount src=$(pwd),target=/home/waterFern,type=bind --name waterfern-frontend -p8000:80 -p8001:443 waterfern/frontend /bin/sh -c "cd /home/waterFern && sg www-data -c 'uwsgi --ini config.ini' & nginx & bash"
