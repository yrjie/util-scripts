import sys,os

if len(sys.argv)<2:
    print 'Usage: file(2 lines) [name1] [name2]'
    exit(1)

nameA='A'
nameB='B'
if len(sys.argv)>=4:
    nameA=sys.argv[2]
    nameB=sys.argv[3]
fi=open(sys.argv[1])
tempA=fi.readline().split('\t')
tempB=fi.readline().split('\t')
fi.close()
setA=set(tempA)
setB=set(tempB)
num1=str(len(setA))
num2=str(len(setA&setB))
num3=str(len(setB))
print '\t'.join([num1, num2, num3])
cmd=' '.join(['R --no-save --slave --args',num1,num2,num3,nameA,nameB,'<~/bin/plotVenn.r'])
os.system(cmd)
