file <- "table_with_frequencies.csv"
myvalues <- read.csv2(file, header = TRUE)
#в csv2 сепаратор это ; 

war_word <- myvalues[which(myvalues$word == "dignity"), 
              -which(names(myvalues) == "word"),]
 
#sub and gsub perform replacement 
#of the first and all matches respectively




barplot(as.numeric(gsub(";", "",war_word)))

