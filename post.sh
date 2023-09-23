#!/bin/bash
handle_interrupt() {
    echo
    exit 0
}


trap handle_interrupt 2
while true
do
    curl -X 'POST' \
  'http://0.0.0.0:8888/upload' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "datetime": "string",
  "title": "string",
  "text": "string"
}'
sleep 3
echo 
done
