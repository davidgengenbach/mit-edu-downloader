#!/usr/bin/env sh

URL=$1
OUT=youtube_urls.txt

if [ -z $URL ]; then
    echo "Usage: $0 url"
    exit 1
fi

./download.py $URL > $OUT
youtube-dl -f bestvideo+bestaudio -a $OUT