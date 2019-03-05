FROM ubuntu

RUN apt update && apt -y install postgresql postgresql-contrib postgresql-client

COPY postgresql.conf    /tmp/postgresql.conf
COPY databaseInit.sql   /tmp/initdb.sql

USER   postgres
# RUN     update-rc.d postgresql enable &&\
#         service postgresql start &&\
ENV PGPASSWORD waterfern
RUN     /etc/init.d/postgresql start &&\
        psql --command "CREATE USER waterfern WITH SUPERUSER PASSWORD 'waterfern';" &&\
        createdb -O waterfern waterfern &&\
        psql -d waterfern -a -f /tmp/initdb.sql
        

RUN echo "host all  all    0.0.0.0/0  md5" >> /var/lib/postgresql/10/main/pg_hba.conf
RUN cp tmp/postgresql.conf /var/lib/postgresql/10/main/postgresql.conf
RUN echo "" >> /var/lib/postgresql/10/main/pg_ident.conf
EXPOSE 5432

VOLUME  ["/etc/postgresql", "/var/log/postgresql", "/var/lib/postgresql"]
CMD ["/usr/lib/postgresql/10/bin/postgres", "-D", "/var/lib/postgresql/10/main", "-c", "config_file=/tmp/postgresql.conf"]






