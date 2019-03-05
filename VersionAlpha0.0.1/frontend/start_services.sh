docker kill waterfern-postgres 
docker rm waterfern-postgres 
docker kill waterfern-frontend
docker rm waterfern-frontend

docker run -d -p5432:5432 --volume settings:/etc/postgresql --volume logs:/var/log/postgresql --volume data:/var/lib/postgresql --name waterfern-postgres psql-server
docker run -it --mount src=$(pwd),target=/home/waterFern,type=bind --name waterfern-frontend -p5000:5000 waterfern/frontend /bin/sh -c 'export LC_ALL=C.UTF-8 && export LANG=C.UTF-8 && cd /home/waterFern/website && echo "npm run build" && cd .. && python3 main.py & bash'