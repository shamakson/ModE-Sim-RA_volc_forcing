#!/bin/bash

for i in {1..200}
do
  lag=1
  diff=`expr $i - $lag`
  echo "lag is $diff"
  echo "call python to generate EVA input $i"
  python loop_mod_EVA_input.py
  cat output.csv | tr  ',' '\n' > out/paleao-ra_$i.txt
  echo "file $i processed"
  rm *.csv
  echo "csv for file $i sucessfully removed"
  sed -i s/Palaeo-ra_$diff.txt/paleao-ra_$i.txt/g EVA_create_initial_file_general.py
  mv EVA_create_initial_file_general.py EVA_create_initial_file_general.sh
  sed -i s/Palaeo-ra_$diff.nc/paleao-ra_$i.nc/g EVA_create_initial_file_general.sh
  mv EVA_create_initial_file_general.sh EVA_create_initial_file_general.py
  python EVA_create_initial_file_general.py
done


