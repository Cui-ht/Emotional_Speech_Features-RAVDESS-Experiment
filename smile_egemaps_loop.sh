#!/bin/bash
# process all .wav file in a folder with opensmile eGeMAPSv01b configuration and store the results in a csv.

indir=$1
outpath=$2
count=1

for wav in $(ls $indir)
do
    ~/opensmile-3.0-osx-x64/bin/SMILExtract -I $indir/$wav -C ~/opensmile-3.0-osx-x64/config/egemaps/v01b/eGeMAPSv01b.conf -csvoutput $outpath -appendcsv 1 -instname $wav
    
    echo "$count file(s) processesed."
    count=$((count+1))
done