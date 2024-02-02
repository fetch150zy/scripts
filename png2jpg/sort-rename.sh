#!/bin/bash

counter=1
for img in $(ls *.jpg | sort -V); do
  mv "$img" "${counter}.jpg"
  ((counter++))
done
