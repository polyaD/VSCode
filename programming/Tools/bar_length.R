rm(list=ls())
library(ggplot2)
library(RColorBrewer)
setwd("D:\\TempC\\Desktop\\temp\\SGR1082")
blank_theme <- theme_minimal()+
  theme(
    axis.title.x = element_blank(),
    axis.title.y = element_blank(),
    panel.border = element_blank(),
    panel.grid=element_blank(),
    axis.ticks = element_blank(),
    plot.title=element_text()
  )
data <- read.table("lengthVSnumber_ra1.txt", sep="\t",header=T)
tf<-"Length of reads distribution"
mydata<-data.frame(data)
mydata
fn<-"lengthVSnumber.png"
fd<-"lengthVSnumber.pdf"
pdf(fd, 8, 6)
#colours=c("blue", "purple","red","violet",  "yellow", "orange","lightblue")
#png(file=fn, bg="transparent",width=800,height=600)

p <- ggplot(mydata,aes(x=mydata$length,y=mydata$reads/100000,fill=mydata$group))+geom_bar(position="dodge",stat="identity")
p+blank_theme
p+scale_x_continuous(limits=c(15, 26),breaks=seq(15, 26, 1))+
  scale_y_continuous(breaks=seq(0, 200, 20))+
  xlab("Length (nt)") + 
  ylab("Number of reads(*100000) ") + 
  labs( title = tf,fill="types")+
  theme(axis.text = element_text( size = 8, hjust = 0, vjust = 0, face = 'bold'))+
  theme(plot.title = element_text(hjust = 0.5,vjust = 0.6,size=14, face="bold"))+
  theme(legend.text = element_text( size = 10, hjust = 3, vjust = 3, face = 'bold'))
dev.off()

png(file=fn, bg="transparent",width=800,height=600)

p <- ggplot(mydata,aes(x=mydata$length,y=mydata$reads/100000,fill=mydata$group))+geom_bar(position="dodge",stat="identity")
p+blank_theme
p+scale_x_continuous(limits=c(15, 26),breaks=seq(15, 26, 1))+
  scale_y_continuous(breaks=seq(0, 200, 20))+
  xlab("Length (nt)") + 
  ylab("Number of reads(*100000) ") + 
  labs( title = tf,fill="types")+
  theme(axis.text = element_text( size = 8, hjust = 0, vjust = 0, face = 'bold'))+
  theme(plot.title = element_text(hjust = 0.5,vjust = 0.6,size=14, face="bold"))+
  theme(legend.text = element_text( size = 10, hjust = 3, vjust = 3, face = 'bold'))
dev.off()

