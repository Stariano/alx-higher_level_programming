#!/bin/bash
# Bash script that takes in a URL and displays all HTTP methods
curl -sIX OPTIONS $1
