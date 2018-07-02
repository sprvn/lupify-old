#!/bin/bash

set -e

sed -i s/80/${LUPIFY_HTTP_PORT}/g /etc/nginx/conf.d/uwsgi-nginx.conf 
sed -i s/443/${LUPIFY_HTTPS_PORT}/g /etc/nginx/conf.d/uwsgi-nginx.conf


exec "$@"
