#!/bin/bash
echo $0

files="$( dirname -- "$0"; )/*.sh"

for file in $files 
do
  if [ $file != $0 ]; then
    $file &
  fi 
done
