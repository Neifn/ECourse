#!/bin/bash
word_counter() {
    # Transforming text into lowercase | printing every word as a new line | removing all non-alphabetic characters | sorting | printig number of occurances
    cat $2 2>/dev/null | tr '[:upper:]' '[:lower:]' | tr ' ' '\n' | sed 's/[^a-z]//g' | sed '/^$/d' | sort | uniq -c | sort $1
}

word_counter2() {
    cat $2 2>/dev/null | tr '[:upper:]' '[:lower:]' | tr ' ' '\n' | sed 's/[^a-z]//g' | sed '/^$/d' | sort $1 | uniq -c 
}
case $1 in 
    -r)
        # Calling function for every argument
        while (( "$#" ))
        do
            word_counter -r "$1"
            shift
        done
    ;;
    -a)
        ARG=$2
        while (( "$#" ))
        do
            if [ $ARG = "-r" ]
            then
                word_counter2 -r $1 
            else
                word_counter2 " " $1
            fi
            shift
        done
    ;;
    *)
        while (( "$#" ))
        do
            word_counter " " $1
            shift
        done
    ;;
esac
