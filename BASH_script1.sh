#!/bin/bash
psql -U postgres -p 5432  db  <<< 'select * FROM public.articles' > /local/files/file$(date +%s)
a=$(find /local/files -type f| wc -l)
if [ "$a" -gt 3 ]
then zip archive /local/files/ -9 -r | mv archive.zip /local/backups/archive$(date +%s) | rm -f /local/files/*
fi
