docker run -d --name redis_server -p 6379:6379 redis_server
rq worker -c rq_settings