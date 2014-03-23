args=commandArgs()
if (length(args)<5){
print("Usage: R --no-save --slave --args infile [name] <plotViolin.R")
q()
}

remove_outliers <- function(x, na.rm = TRUE, ...) {
  qnt <- quantile(x, probs=c(.25, .75), na.rm = na.rm, ...)
  H <- 2 * IQR(x, na.rm = na.rm)
  y <- x
  y[x < (qnt[1] - H)] <- NA
  y[x > (qnt[2] + H)] <- NA
  y
}

library(vioplot)
infile=args[5]
name=""
if (length(args)>=6){
	name=args[6]
}
outfile='temp.png'
fi=file(infile,open="r")
dat=list()
while (length(line<-readLines(fi,n=1,warn=FALSE))>0){
	vec=strsplit(line,"\t")
	lenv=length(vec[[1]])
	cname=vec[[1]][1]
	vec=list(as.numeric(vec[[1]][2:lenv]))
#	dat[cname]=vec
	dat[cname]=list(remove_outliers(vec[[1]]))
	print(summary(dat[[cname]]))
}
print(names(dat))
png(outfile)
#boxplot(dat,main=name,range=0)
vioplot(c(123,111,2,1,1,1,111,111),c(121,213,16,164),col="cyan",na.rm=TRUE)
dev.off()
