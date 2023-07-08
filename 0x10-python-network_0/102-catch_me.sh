#!/bin/bash
# script that was a fun effort in breaking to http protocols on holberton serve
curl -s -o /dev/null -w "%{body_response}" "$1"
