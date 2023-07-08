#!/bin/bash
# bash script to display status code of server
curl -LI "$1" -o /dev/null -w '%{http_code}\n' -s
