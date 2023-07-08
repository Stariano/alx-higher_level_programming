#!/bin/bash
# bash script for posting json data files and testing a server
curl -sX POST "$1" -d "$2"
