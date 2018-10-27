FROM centos:latest
MAINTAINER Kevin Gustafsson
RUN yum install epel-release -y
RUN yum clean all
RUN yum update -y
#COPY . /app
VOLUME $(pwd)/lupify:/app
#VOLUME $(pwd):/app
WORKDIR /app
RUN yum install python-pip -y
RUN pip install flask
EXPOSE 5000:5000
ENTRYPOINT ["python"]
CMD ["lupify/lupify.py"]
#CMD ["flask_app.py"]
