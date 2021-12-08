#!/bin/bash 
source test.sh
while true [[ $now_files -gt $max_files ]] | [[ $now_size -gt $max_size ]] 
do
echo "number of files in /local/backups directory is more than $a files, total size of /local/backups directory is more than $b bytes " | mail -s "Test subject" root
sleep 30
done
