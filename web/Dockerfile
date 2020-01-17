FROM ubuntu:18.04

RUN apt-get -y update
RUN apt install python3.5 python3-pip -y
RUN pip3 install --upgrade pip

ADD app /app
ADD a.sh /app/a.sh
RUN chmod 755 /app/a.sh

RUN pip3 install Flask SQLAlchemy flask-sqlalchemy PyMySQL Flask-Migrate

WORKDIR /app
CMD ./a.sh