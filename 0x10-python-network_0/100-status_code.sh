#!/bin/bash
# bash script to display status code of server
curl -sIo /dev/null -w '%{http_code}' "$1"
