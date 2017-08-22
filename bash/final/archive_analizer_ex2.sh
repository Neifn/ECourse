#!/bin/bash
tarcomparison(){
    # Compare archives line by line
    tar -tf $1 | while read line
    do
        if ! tar -tf $2 | grep -x $line > /dev/null
        then
            echo ${line}
        fi
    done
}

# Checking if files exist and tar.gz archives
if [ $# = 2 ] && file $1 | grep 'gzip compressed data' > /dev/null && file $2 | grep 'gzip compressed data' > /dev/null
then
    # Remove string if there is "/" inside the string.
    ITEMS=`tarcomparison $1 $2 | grep "/$"`
    tarcomparison $1 $2 | while read line
    do
        for item in ${ITEMS}
        do
            if ! [[ $line =~ ${item}.*. ]]
            then
                echo $line
            fi
        done
    done
else
    echo "Files do not exist or are not in tar.gz archive"
    exit 1
fi
