#!/bin/bash

# Exit in case of error
set -e
set -x

docker compose up $1 $2 $3