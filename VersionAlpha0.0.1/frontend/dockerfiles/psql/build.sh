docker kill waterfern-postgres
docker rm waterfern-postgres
docker volume rm settings
docker volume rm logs
docker volume rm data

docker build --rm=true -t psql-server .

