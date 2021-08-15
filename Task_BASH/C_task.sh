#!/bin/bash
log_file=backup_log
rsync --delete --quiet -ahc important/ backup/ --log-file=$log_file --remote-option=--log-file=$log_file --remote-option=--log-file-format='%o %f'

