docker kill psql-server
docker rm psql-server
docker volume rm psql-volume 

docker volume create psql-volume 
docker build --rm=true -t psql-server .

