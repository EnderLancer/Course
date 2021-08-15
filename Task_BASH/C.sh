#!/bin/bash
if [ $# -lt 2 ]; then
  echo "Need two arguments, directories 'from' and 'to'."
fi
log_file_raw=backup_log_raw
rsync --delete --quiet -ahc $1 $2 --log-file=$log_file_raw --remote-option=--log-file=$log_file_raw --remote-option=--log-file-format='%o %f'
#cat $log_file
log_file=backup_log
sed -e '/receiving file list/d;
/building file list/d;
/sent [0-9]* bytes *received [0-9]* bytes/d;
/ .\/$/d;
/ .$/d;
s/..+++++++++/append/' $log_file_raw >> $log_file
rm $log_file_raw

