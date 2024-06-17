#!/bin/sh
docker exec -it [$1] /bin/bash -c "echo 'Bonjour, Docker Volumes!' > /data/bonjour.txt"
docker stop [$1]
docker start [$1]
docker exec -it [$1] /bin/bash -c "cat /data/bonjour.txt"