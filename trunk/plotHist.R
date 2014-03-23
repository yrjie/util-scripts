Args<-commandArgs()
if (length(Args)<5){
	print("Usage: R --no-save --slave --args infile")
	q()
}
data <- read.table(Args[5], header=FALSE, sep ="\t")
png(paste(gsub("\\$","_",Args[5]),".png",sep=""))
opar=par(ps=18)
hist(data[,1],breaks=50,main="",col='red',xlab="x value", ylab="Counting")
