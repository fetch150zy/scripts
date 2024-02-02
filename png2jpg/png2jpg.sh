#! /usr/bin/bash

for img in *.jpg; do
    magick "$img" "${img%.jpg}.png"
done

rm ./*.jpg
