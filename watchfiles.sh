#!/bin/bash
IFS=$'\n'

DIR=./

EXP='%TD %TT %p\n'

ANTERIOR=`find ${DIR} -type f -printf '"%TD %TT %p\n"'`

while true ; do
  ATUAL=`find ${DIR} -type f -printf '"%TD %TT %p\n"'`
  DIFERENCA=`diff --changed-group-format='%<' --unchanged-group-format='' <(echo  "${ATUAL}") <(echo "${ANTERIOR}")`
  for file in ${DIFERENCA}; do
    echo "$file novo ou alterado"
  done;
  ANTERIOR=${ATUAL}
done;  

