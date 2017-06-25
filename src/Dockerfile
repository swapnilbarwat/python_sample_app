# The base image
FROM python:2.7
RUN pip install tornado
RUN mkdir -p /usr/local/server && cd /usr/local/server
ENV TERM=xterm
COPY sample_app.py  /usr/local/server
WORKDIR /usr/local/server/

CMD python sample_app.py
