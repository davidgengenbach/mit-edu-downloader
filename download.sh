#!/usr/bin/env sh

OUT=youtube_urls.txt
./download.py > $OUT
youtube-dl -f bestvideo+bestaudio -a $OUT