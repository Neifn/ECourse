#!/bin/bash

recursive_search ()
{
    # Variable assumes value from directory contents
    for file in $( ls -d --group-directories-first $2/* 2>/dev/null )
    do
        # Check if variable is directory
        if [ -d $file ]
        then
            # Calling recurisve_search with variable as an argument
            recursive_search $1 $file
        # Check if variable is a symbolic link
        elif ls -ld $file | grep ^l >/dev/null
        then
            # Check first argument is "r" (remove) and removes broken links if it is
            if [ $1 = "r" ]
            then
                if [ ! -f $file ]
                then	
                    echo $file
                    rm $file
               fi
            # Check first argument is "a" (list all) and lists all links including broken ones
            elif [ $1 = "a" ]
                then 
                ls -ld $file | grep ^l | awk '{print $9}'
            else
                echo "Enter valid arguments"
                exit 1
            fi
       fi
    done
}

if [ "$#" -ne 1 ] && [ "$#" -ne 2 ]
then
    echo "Enter at least 1 or 2 arguments"
elif [ ! "$#" -ne 1 ]
then
    recursive_search $1 .
else
    recursive_search $1 $2
fi
