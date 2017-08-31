#!/bin/bash
script_search () {
   find $1 -name "*" 2>/dev/null | while read line
   do
       if [ $2="f" ]
       then
           if head -n 1 $line 2>/dev/null | grep "#!" | grep -e "/$3$" > /dev/null
           then
               echo $line $( head -n 1 $line | awk '{print $NF}' FS=/ )
           fi
       else
           if  head -n 1 $line 2>/dev/null | grep "#!" > /dev/null
           then
               echo $line $( head -n 1 $line | awk '{print $NF}' FS=/ )
           fi
       fi
   done
}
non_recursive () {
   find $1 -maxdepth 1 -name "*" 2>/dev/null | while read line
   do
       if [ $2="f" ]
       then
           if head -n 1 $line 2>/dev/null | grep "#!" | grep -e "/$3$" > /dev/null
           then
               echo $line $( head -n 1 $line | awk '{print $NF}' FS=/ )
           fi
       else
           if head -n 1 $line 2>/dev/null | grep "#!" > /dev/null
           then
               echo $line $( head -n 1 $line | awk '{print $NF}' FS=/ )
           fi
       fi
   done
}

case $1 in
    -n)
        case $2 in
            -f)
                non_recursive $4 f $3
            ;;
            *)
                non_recursive $2
            ;;
        esac 
    ;;
    *)
        case $1 in
            -f)
                script_search $3 f $2
            ;;
            *)
                script_search $1
            ;;
        esac
    ;;
esac
