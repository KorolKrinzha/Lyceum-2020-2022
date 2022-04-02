import csv


#Чтение
with open('addresses.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
        print(' '.join(row), '\n')

#Запись
with open('addresses.csv', 'a', newline='') as csvfile:        
    spamwriter = csv.writer(csvfile, delimiter=' ',
                            quotechar=',', quoting=csv.QUOTE_MINIMAL)
    
    # Рандомная запись
    newrow = ['Oliver', 'Tree', '220 Brighton st.', 'LAndside', 'Vladimir', str('12345')]
    #
    
    spamwriter.writerow(newrow) 
    print("###############################")
    print(newrow)

'''
with open('addresses.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar=',')
    for row in spamreader:
        
        print(' '.join(row), '\n')    
'''      