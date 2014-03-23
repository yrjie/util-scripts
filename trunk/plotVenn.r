args=commandArgs()
if (length(args)<9){
    print("Usage: R --no-save --slave --args n1 n12 n2 name1 name2 / n1 n2 n3 n12 n13 n23 n123 name1 name2 name3 <plotVenn.r")
    q()
}
filename='ven1.png'
#if (length(args)>=10)
#	filename=args[10]
require(VennDiagram)
png(filename,width=800,height=600)
if (length(args)==9){
n1=as.numeric(args[5])
n12=as.numeric(args[6])
n2=as.numeric(args[7])
name1=args[8]
name2=args[9]
num1=3239
num2=19197
num3=20814
v1<-venn.diagram(list(A = 1:n1, B = (n1-n12+1):(n1+n2-n12)),fill = c("red", "green"),alpha = c(0.5, 0.5), cex = 2,cat.fontface=4, cat.cex=3, lty =1, fontfamily =3,filename=NULL, category=c(name1, name2),margin=0.2);
grid.draw(v1)
} else{
    v2 <- draw.triple.venn(
	area1 = as.numeric(args[5]),
	area2 = as.numeric(args[6]),
	area3 = as.numeric(args[7]),
	n12 = as.numeric(args[8]),
	n13 = as.numeric(args[9]),
	n23 = as.numeric(args[10]),
	n123 = as.numeric(args[11]),
	category = c(args[12], args[13], args[14]),
	fill = c("blue", "red", "green"),
	scaled=TRUE,
	cex=2,
	cat.fontface=4,
	cat.cex=3,
	margin=0.2)
    grid.draw(v2)
}
dev.off()
