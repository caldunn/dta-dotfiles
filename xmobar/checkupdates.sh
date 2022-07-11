#!/bin/sh
update=$(checkupdates | wc -l)
if [ $update -gt 0 ]
then 
 echo $update "updates" 
else 
  echo "Fully Updated"
fi

