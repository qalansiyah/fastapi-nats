#!/bin/sh
curl -X 'GET' \
  'http://0.0.0.0:8888/result' \
  -H 'accept: application/json'
echo
