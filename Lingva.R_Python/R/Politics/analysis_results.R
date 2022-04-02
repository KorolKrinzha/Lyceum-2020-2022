file <- "table_with_frequencies.csv"
myvalues <- read.csv2(file, header = TRUE)
#в csv2 сепаратор это ; 

politics<-tail(names(myvalues), -1)
politics<-c("JFK","MLK","Reagan","MLK",
            "Churchill","Churchill",
            "Churchill","Hirohito","Hirohito",
            "Yeltsin","Yeltsin","LKY","LKY",
            "LKY","Milosevic","Milosevic")
dignity_word <- myvalues[which(myvalues$word == "dignity"), 
              -which(names(myvalues) == "word"),]
 
war_word <- myvalues[which(myvalues$word == "war"), 
                         -which(names(myvalues) == "word"),]

prosperity_word <- myvalues[which(myvalues$word == "prosperity"), 
                     -which(names(myvalues) == "word"),]
					 
					 
nation_word <- myvalues[which(myvalues$word == "nation"), 
                     -which(names(myvalues) == "word"),]

government_word <- myvalues[which(myvalues$word == "government"), 
                     -which(names(myvalues) == "word"),]

barplot(as.numeric(gsub(";", "",dignity_word)), 
        main = "Использование слова dignity",
        ylab = "Частота",
        col = rainbow(16),
        names.arg = politics,
        horiz = FALSE,
        las = 2)

barplot(as.numeric(gsub(";", "",war_word)), 
        main = "Использование слова war",
        ylab = "Частота",
        col = rainbow(16),
        names.arg = politics,
        horiz = FALSE,
        las = 2)

barplot(as.numeric(gsub(";", "",prosperity_word)), 
        main = "Использование слова prosperity",
        ylab = "Частота",
        col = rainbow(16),
        names.arg = politics,
        horiz = FALSE,
        las = 2)

barplot(as.numeric(gsub(";", "",nation_word)), 
        main = "Использование слова nation",
        ylab = "Частота",
        col = rainbow(16),
        names.arg = politics,
        horiz = FALSE,
        las = 2)

barplot(as.numeric(gsub(";", "",government_word)), 
        main = "Использование слова government",
        ylab = "Частота",
        col = rainbow(16),
        names.arg = politics,
        horiz = FALSE,
        las = 2)		
