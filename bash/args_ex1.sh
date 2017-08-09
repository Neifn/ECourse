#!/bin/bash 
if [ $# -lt 1 ]
  then
    echo "enter at least one argument"
    exit 1

fi
for i
do 
    echo $i 
done

count=0
until [ $count == $# ]
do
    count=$((count+1))
    echo ${!count}
done

while (( $# ))
do
   echo $1
   shift
done

