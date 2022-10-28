#!/usr/bin/env bash
# This scripts sets up my web servers for the deployment of web_static

apt-get -y update
apt-get -y install nginx

mkdir -p /data/
mkdir -p /data/web_static/
mkdir -p /data/web_static/releases/
mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/releases/test/
echo 'Holberton School' | sudo tee /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu /data/
chgrp -R ubuntu /data/
sudo sed -i "/server_name _;/ a\\\trewrite ^/redirect_me http://www.google.com permanent;" /etc/nginx/sites-available/default
sudo sed -i '/server_name _/a location /hbnb_static {alias /data/web_static/current; }' /etc/nginx/sites-available/default
sudo sed -i '/server_name _/a error_page 404 /404.html; location = /404.html {root /var/www/error/;internal; }' /etc/nginx/sites-available/default
sudo sed -i "s/include \/etc\/nginx\/sites-enabled\/\*;/include \/etc\/nginx\/sites-enabled\/\*;\n\tadd_header X-Served-By \"$HOSTNAME\";/" /etc/nginx/nginx.conf
service nginx restart
