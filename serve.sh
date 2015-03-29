#!/bin/bash
set -e
( sleep 3 && open 'http://localhost:3000/' ) &
jekyll serve --watch --host localhost --port 3000
