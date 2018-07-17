#!/bin/bash

set -e

sed -i s/HTTP_PORT_TMP/${LUPIFY_HTTP_PORT}/g /etc/nginx/conf.d/uwsgi-nginx.conf 
sed -i s/HTTPS_PORT_TMP/${LUPIFY_HTTPS_PORT}/g /etc/nginx/conf.d/uwsgi-nginx.conf

sed -i s/\<mongodb_uri\>/${LUPIFY_MONGODB_URI}/g /lupify/lupify/config.ini
sed -i s/\<mongodb_user\>/${LUPIFY_MONGODB_USER}/g /lupify/lupify/config.ini
sed -i s/\<mongodb_pass\>/${LUPIFY_MONGODB_PASS}/g /lupify/lupify/config.ini

exec "$@"
