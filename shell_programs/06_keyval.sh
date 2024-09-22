#!/bin/bash
declare -A myarr
myarr=([name]="pranshant" [age]=30 [city]="Paris")

echo "My name is ${myarr[name]} and age${myarr[age]} and city ${myarr[city]}"
