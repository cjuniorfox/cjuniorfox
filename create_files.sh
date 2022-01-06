#!/bin/sh

intfile=0;

for i in {0..10000}; do
  echo $i
  while [ -f "$intfile.txt" ]; do
    intfile=$((intfile + 1));
  done;
  touch "$intfile.txt";
done;
    
