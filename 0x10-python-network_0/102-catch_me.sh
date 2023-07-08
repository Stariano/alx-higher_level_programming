#!/bin/bash
# script that was a fun effort in breaking to http protocols on holberton serve
curl -sX PUT -H "origin:School" -d "user_id=98" 0.0.0.0:5000/catch_me_3
