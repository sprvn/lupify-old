FROM centos:latest

#RUN pip install flask
#RUN pip install flask_login
#RUN pip install pymongo
#RUN pip install flask_wtf
RUN yum clean all
RUN yum update -y
RUN yum install epel-release -y
RUN yum install nginx -y
RUN yum install python34 -y
RUN yum install python34-pip -y
RUN yum install python34-devel -y
RUN yum install gcc -y
RUN pip3 install --upgrade pip
RUN pip3 install flask
RUN pip3 install flask_login
RUN pip3 install pymongo
RUN pip3 install uwsgi

#RUN rm -rf /usr/bin/python
#RUN ln -s /usr/bin/python3 /usr/bin/python

RUN rm /etc/nginx/nginx.conf
#RUN rm /etc/nginx/conf.d/default.conf
#RUN rm /etc/nginx/conf.d/*

COPY configs/nginx.conf /etc/nginx/
COPY configs/uwsgi-nginx.conf /etc/nginx/conf.d/

COPY ./myapp /app