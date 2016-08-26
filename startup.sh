#!/bin/bash
test -n "$1" && ARG=$(echo $1 | tr [a-z] [A-Z])
if [ "$ARG" == "START" ]; then
  if [ -x /usr/local/bin/uwsgi ]; then
      exec /usr/local/bin/uwsgi --ini-paste shavar.ini --paste-logger --uid 10001 --gid 10001
  else
    echo "uwsgi is not installed"
    exit
  fi
else
  echo "Invalid option specified: ARG=$ARG"
  exit
fi  
