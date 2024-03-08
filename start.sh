#!/bin/bash
cd "$(dirname "$0")"

python3 ./web/backend/server.py &
echo "$!"

python3 ./web/frontend/server.py &
echo "$!"

python3 installer.py &
echo "$!"