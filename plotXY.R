args=commandArgs()
if (length(args)<5){
print("Usage: R --no-save --slave --args infile [infile2] <plotXY.R")
q()
}
infile=args[5]
outfile='temp.png'
dat=as.matrix(read.table(infile,sep='\t'))
x=dat[,1]
if (length(args)>=6){
	y=as.matrix(read.table(args[6],sep='\t'))[,1]
} else y=dat[,2]
png(outfile)
plot(x,y,xlab='regionVal',ylab='validation',lty=1)
title('validation-regionVal correlation')
corr=cor(x,y)
print(corr)
mtext(paste('correlation=',corr,sep=''),side=3,line=0,cex=2)
dev.off()
