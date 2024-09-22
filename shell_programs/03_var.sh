#!/bin/bash
a=10
name="Hari"
age=30
echo "My name is $name and my age is $age"
echo "Number is $a"
# varaible to store output of command
HOSTNAME = $(hostname)
echo "Hostname is $HOSTNAME"
# if want to change the value of name it overide the value
name=ram
echo "My name is $name and my age is $age"
