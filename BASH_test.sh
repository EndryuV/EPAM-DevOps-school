#!/bin/bash 
max_size=2000
max_files=10
now_size=$(du -b /local/backups/ | sed s/[^0-9]//g)
now_files=$(find /local/backups -type f | wc -l) 
a=$(($now_files - $max_files))
b=$(($now_size - $max_size))
