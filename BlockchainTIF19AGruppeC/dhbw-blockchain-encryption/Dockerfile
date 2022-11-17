# syntax=docker/dockerfile:1

FROM python:3.10.6-slim-buster

WORKDIR /python-docker

COPY requirements.txt requirements.txt
RUN apt-get update
RUN pip install --upgrade pip && apt install python3-pip -y && apt install mariadb-client -y && apt install libmariadb-dev-compat -y
RUN apt install build-essential -y
RUN apt install wget -y && apt install curl -y && wget https://downloads.mariadb.com/MariaDB/mariadb_repo_setup && echo "733cf126b03f73050e242102592658913d10829a5bf056ab77e7f864b3f8de1f  mariadb_repo_setup" | sha256sum -c -
RUN chmod +x mariadb_repo_setup
RUN ./mariadb_repo_setup --mariadb-server-version="mariadb-10.6"
RUN rm mariadb_repo_setup
RUN  apt install libmariadb3 libmariadb-dev -y


RUN pip install -r requirements.txt

COPY *.py ./

EXPOSE 45675

CMD [ "python", "-m" , "flask", "run", "--host=127.0.0.1"]
