#!/bin/bash

input="./input"
output="./output"

for filename in $input/{normal,italic}/*.{woff,woff2}; do
	./woff2/woff2_decompress $filename
done

if [ ! -d "./.venv" ] && [ ! -d "./venv" ]; then
	python3 -m venv .venv
fi

source ./.venv/bin/activate
python3 -m pip install -r requirements.txt
python3 to_static.py
