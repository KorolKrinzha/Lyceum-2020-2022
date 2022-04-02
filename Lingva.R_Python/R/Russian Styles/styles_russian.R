install.packages('stylo')
library(stylo)
path <- file.path(paste(getwd()))
print(path)
setwd(path)
stylo(encoding = "UTF-8", corpus.lang = "Other")



