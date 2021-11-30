import csv
import random

dictionary = {}

with open('collage2000.csv', 'r', encoding='UTF8') as csvfile:
    reader = csv.reader(csvfile)
    reader.__next__()
    for row in reader:
        if(row[0] in dictionary):
            dictionary[row[0]].append((row[1], row[2]))
        else:
            dictionary[row[0]] = [(row[1], row[2])]
    
s = input("day what? : ")
day = 0
if(s == "random"):
    day = random.randint(1, 31)    
else:
    day = int(s)
if(day < 10):
    day = "0{}".format(day)

while True:
    for (word, mean) in dictionary["day{}".format(day)]:
        w = input("What does ' {} ' Mean? : ".format(word))
        if(mean.find(w) != -1):
            print("\t정답")
        else:
            print("\t오답")
            print(mean)