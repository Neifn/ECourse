#!/bin/bash
recursive_change ()
{
    if [ -e $1 ]
    then
    # Variable assumes value from directory contents
      for file in $( ls -d --group-directories-first $1/* )
      do
        # Check if variable is directory
        if [ -d $file ]
        then
            # Calling recurisve_search with variable as an argument
            recursive_change $file $2 $3 $4
        # Check if variable is a symbolic link
        elif ls -ld $file | grep ".*\.$3$"  >/dev/null
        then
            # Check first argument is "r" (remove)
            case $2 in
            -r)
                if [ "$#" -ne 3 ]
                then
                    echo "Illegal number of parameters"
                    exit 1
                else
                    rm $file
                    echo "$file has been removed"
                fi
            # Check first argument is "c" (copy)
            ;;
            -c)
                if [ "$#" -ne 4 ]
                then
                    echo "Illegal number of parameters"
                    exit 1
                else
                    # Replacing file name with $4 extension
                    NEWNAME=$( echo ${file} | sed "s/\..*/.$4/" )
                    cp $file $NEWNAME
                    echo "Name of a copy of $file => $NEWNAME"
                fi
            ;;
            -m)
                if [ "$#" -ne 4 ]
                then
                    echo "Illegal number of parameters"
                    exit 1
                else
                    NEWNAME=$( echo ${file} | sed "s/\..*/.$4/" )
                    mv $file $NEWNAME
                    echo "$file => $NEWNAME "
                fi
            ;;
            *)
                echo "Wrong parameter"
                exit 1
            esac
       fi
    done
  else
    echo "No such file or directory"
    exit 1
  fi
}
# Removing "." in third and fourth arguments if there is one
VALUE=$( echo $3 | sed 's/^\.//' )
VALUE2=$( echo $4 | sed 's/^\.//' )
recursive_change $1 $2 $VALUE $VALUE2
