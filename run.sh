#!/usr/bin/env bash
echo "start run flask server"

flask --app server run --host=0.0.0.0

echo "flask server end"
