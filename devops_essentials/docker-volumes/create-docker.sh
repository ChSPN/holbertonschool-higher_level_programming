#!/bin/sh
docker build -t docker-volume .
docker run -d -v /tmp/data:/data docker-volume