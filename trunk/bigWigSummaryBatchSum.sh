#!/bin/bash

if [ $# -lt 2 ]
then
    echo "Usage: bigWig bed"
    exit
fi

tmp1=/tmp/temp1$RANDOM
tmp2=/tmp/temp2$RANDOM
bigWigSummaryBatch $1 $2 1 >$tmp1
bigWigSummaryBatch $1 $2 1 -type=coverage >$tmp2
paste $tmp1 $tmp2 |awk '{if ($2>0) print $1/$2; else print 0}'

rm $tmp1 $tmp2
