#!/bin/bash
if [ -z "$1" ]; then
	echo "USEGE : $0 <URL>"
	EXIT 1
fi
URL=$1
size=$(curl -s -o /dev/null -w '%{size_download}'"$URL")
echo "$size"
