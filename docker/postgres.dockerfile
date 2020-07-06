FROM postgres:12

COPY ./postgres_init.sql /docker-entrypoint-initdb.d/