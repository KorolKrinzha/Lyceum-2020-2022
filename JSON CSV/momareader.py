
'''
import csv

with open ('moma.csv', 'r') as fp:
    reader = csv.reader(fp, delimiter = ',', quotechar = ' ')
    data_read = [row for row in reader][1:]
 
for person in data_read:
    #print(person[1], 'is', person[4], ' ', person[3])
    print(person)
'''
#FAILED ATTEMPT



import csv
with open('moma.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row['DisplayName'], row['Gender'], row['ArtistBio'], sep = ";")