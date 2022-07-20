#!/bin/sh

for f in $(ls thumb0*.jpg)
do 
	echo $f
	convert -extract 6x1080+1150+0 $f ./out/$f.conv.jpg

done
