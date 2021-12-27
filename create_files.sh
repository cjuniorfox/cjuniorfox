#!/bin/sh

intfile=0;

for i in {0..1000}; do
  while [ -f "$intfile.txt" ]; do
    intfile=$((intfile + 1));
  done;
  touch "$intfile.txt";
done;
    
