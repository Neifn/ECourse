#!/bin/bash

recursive(){
    echo -e "\e[94m${1}\e[0m"
    FILES=$(find $1 -maxdepth 1 -type f | sort)
    DIRECTORIES=$(find $1 -maxdepth 1 -type d | tail -n +2 | sort)
    for item in $FILES
    do
        if ! file -i "$item" | grep bit > /dev/null
        then
            if wc -l $item 2>/dev/null >/dev/null
            then
                echo -e "  \033[32m`wc -l $item`\e[0m"
            fi
        fi
    done
    for item in $DIRECTORIES
    do
        recursive $item | sed 's/^/  /'
    done
}

recursive $1
