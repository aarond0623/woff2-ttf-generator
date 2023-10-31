#!/bin/bash

input="./input"
output="./output"

for filename in $input/{normal,italic}/*.{woff,woff2}; do
	./woff2/woff2_decompress $filename
done
