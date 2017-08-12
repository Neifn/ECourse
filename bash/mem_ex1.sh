#/bin/bash
df | sed 1d | while read line
do
MEMORY=$(echo $line | awk '{print $5}' | sed 's/%//')
NAME=$(echo $line | awk '{print $1}' )
MOUNT=$(echo $line | awk '{print $6}' )
if (( $MEMORY >= 90 ))
then
    echo "Disk usage of the device $NAME ($MOUNT) is too high and is equal to ${MEMORY}%"
else
    echo "Disk usage of the device $NAME ($MOUNT) is within limits and is equal to ${MEMORY}%"
fi
done
