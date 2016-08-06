FROM alpine:latest
RUN apk add --no-cache bash git nginx uwsgi uwsgi-python py-pip \
	&& pip install --upgrade pip \
	&& pip install flask
ENV APP_DIR /src
EXPOSE 80
