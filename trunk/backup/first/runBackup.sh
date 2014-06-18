if [ $# -lt 1 ]
then
    echo 'Usage: message'
    exit
fi

echo $1
cp ~/*/*.sh ~/bin/backup/first/
#cp ~/*/*.py ~/bin/backup/first/
#cp ~/*/*.R ~/bin/backup/first/
#find ~/ -name *.sh -path ~/bin -prune -o -exec cp {} ~/bin/backup/all/ \;
#find ~/ -name *.py -path ~/bin -prune -o -exec cp {} ~/bin/backup/all/ \;
#find ~/ -name *.R -path ~/bin -prune -o -exec cp {} ~/bin/backup/all/ \;
cd ~/bin
svn add backup/*
svn commit -m $1
