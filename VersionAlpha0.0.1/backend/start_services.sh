docker kill redis_server
docker rm redis_server
docker kill waterfern
docker rm waterfern

docker run -d --name redis_server redis_server
docker run -it --mount src=$(pwd),target=/home/waterFern,type=bind --link redis_server --name waterfern -p 12345:443 waterfern/backend bin/sh -c "export LC_ALL=C.UTF-8 && export LANG=C.UTF-8 && cd home/waterFern && rq worker -c rq_settings & cd home/waterFern && sg www-data -c 'uwsgi --ini config.ini' & nginx & bash"