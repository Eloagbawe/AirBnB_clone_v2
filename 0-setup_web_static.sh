#!/usr/bin/env bash
# This scripts sets up my web servers for the deployment of web_static

sudo apt-get -y update
sudo apt-get -y install nginx

sudo mkdir -p /data/
sudo mkdir -p /data/web_static/
sudo mkdir -p /data/web_static/releases/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
sudo touch /data/web_static/releases/test/index.html
echo 'Testing html' | sudo tee /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu /data/
sudo chgrp -R ubuntu /data/
sudo chown -R "$USER":"$USER" /var/www
sudo mkdir -p /var/www/error
echo "Ceci n'est pas une page" | sudo tee /var/www/error/404.html
sudo sed -i "/server_name _;/ a\\\trewrite ^/redirect_me http://www.google.com permanent;" /etc/nginx/sites-available/default
sudo sed -i '/server_name _/a location /hbnb_static {alias /data/web_static/current; }' /etc/nginx/sites-available/default
sudo sed -i '/server_name _/a error_page 404 /404.html; location = /404.html {root /var/www/error/;internal; }' /etc/nginx/sites-available/default
sudo sed -i "s/include \/etc\/nginx\/sites-enabled\/\*;/include \/etc\/nginx\/sites-enabled\/\*;\n\tadd_header X-Served-By \"$HOSTNAME\";/" /etc/nginx/nginx.conf
sudo service nginx restart