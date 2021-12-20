#!/bin/bash
psql -U postgres -p 5432  db  <<< 'select * FROM public.articles' > /local/files/file$(date +%s)
a=$(find /local/files -type f| wc -l)
if [ "$a" -gt 3 ]
then tar -cvf /local/backups/archive$(date +%s) /local/files/
fi
