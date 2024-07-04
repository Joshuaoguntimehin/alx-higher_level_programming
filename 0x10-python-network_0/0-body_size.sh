#!/bin/bash
# 0-body_size.sh
if [ -z "$1" ]; then
    echo "USAGE: $0 <URL>"
    exit 1
fi

URL=$1

# Check if the URL starts with "http://" or "https://"
if [[ ! "$URL" =~ ^https?:// ]]; then
    URL="http://$URL"
fi

# Use curl to get the size of the response body in bytes
size=$(curl -s -o /dev/null -w '%{size_download}' "$URL")
echo "Size: $size bytes"0-body_size.sh

