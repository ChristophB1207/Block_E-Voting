FROM ubuntu 
RUN apt update -y
RUN apt dist-upgrade -y
RUN apt install  apache2 -y
RUN apt install  apache2-utils -y
RUN apt clean -y
COPY index.html /var/www/html
COPY index2.html /var/www/html
COPY index3.html /var/www/html
COPY css/ /var/www/html
COPY js/ /var/www/html
EXPOSE 80
CMD apachectl -D FOREGROUND
