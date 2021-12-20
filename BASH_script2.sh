#!/bin/bash 
source test.sh
while true [[ $now_files -gt $max_files ]] | [[ $now_size -gt $max_size ]] 
do
    if [[ $now_files -gt $max_files ]] 
    then 
    echo "Number of files in /local/backups directory is more than $a files." | mail -s "TNumber of files $a files" root@db.lan
    fi
    if [[ $now_size -gt $max_size ]] 
    then 
    echo "Total size of /local/backups directory is more than $b bytes " | mail -s "Total size $b bytes" root@db.lan
    fi
sleep 360
done
