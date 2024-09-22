#!/bin/bash

# creating in array in shell scripts
myarr=(1 3 3.4 "Hello" "e23")

echo "Value of array at index 2 ${myarr[2]}"

# if you want display all the values in array

echo "All the values in array ${myarr[*]}"
# if we want to find the length of array

echo "length of array ${#myarr[*]}"

# if we find the values from certain index isme index se start hokar kitne value chayie vo dalte 

echo "Values start from index 2 to 4 ${myarr[*]:2:3}"

# if we want to add some values in existing array
myarr+=(new 56 25)
echo "All the values in array ${myarr[*]}"

