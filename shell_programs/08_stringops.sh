#!/bin/bash
str="Hey buddy, How are you?"

#length of string
len="${#str}"
echo "length is $len"

#upper and lower case of str
echo  "Upper --------${str^^}"
echo  "Lower --------${str,,}"
#slicing pof str

echo "sliced string ${str:4:5}"
