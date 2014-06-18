if [ $# -lt 1 ]
then
    echo 'Usage: bedfile'
    exit
fi
awk '{if (NR==1) printf "len"; printf "\t"$3-$2}' $1 >temp.dat
R --no-save --slave --args temp.dat <~/bin/plotBox.R
