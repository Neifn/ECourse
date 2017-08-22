#!/bin/bash
backup() {
    # Checking if $1 and $2 represent valid files or directories
    if [ -e $1 ] && [ -d $2 ]
    then
        COUNTER=0
        while true
        do
            # Checking if archive with the name "$1\_$COUNTER.tar.gz" exists in the given directory if it does adding 1 to COUNTER
                                  # Removing last symbol of a string if it's a "/"
            if ls -d $( echo $2 | sed 's/\/$//' )/* | grep -e "$(basename $1)_$COUNTER.tar.gz$" > /dev/null
            then
                let COUNTER=COUNTER+1
            else
                # If archive does not exist - creating it and exiting theloop
                tar -P -cvzf $( echo $2 | sed 's/\/$//' )/$( basename $1 )_$COUNTER.tar.gz $1 > /dev/null
                echo "You can find new archive in $2"
                break
            fi
        done
    else
        echo "No such file or directory"
        exit 1
    fi
}

# Checking the number of arguments
if ! [ "$#" -ne 2 ]
then
    backup $1 $2
elif ! [ "$#" -ne 1 ]
then
    backup $1 .
else
    echo "Enter 1 or 2 arguments"
    exit 1
fi
