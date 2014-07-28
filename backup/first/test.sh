echo $1 $2 $3 \'$1\'

echo $# $*
echo $@
if [ $# -lt 2 ]
then
    echo 321
fi
echo "not lt 2"
