install.packages('stylo')
library(stylo)
getwd()
a <- file.path(paste(getwd()),'corpus' )
print(a)
setwd(a)
stylo(encoding = "UTF-8", corpus.lang = "Other")



