FROM ubuntu

RUN apt-get -y update && apt-get -y install nginx

COPY sites-enabled/ /etc/nginx/sites-enabled

EXPOSE 80/tcp

CMD ["/usr/sbin/nginx", "-g", "daemon off;"]