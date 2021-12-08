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

wordsByDay = dictionary["day{}".format(day)]
print("최소 {}개는 무한 반복으로 외운다".format(len(wordsByDay)))
wrongs = []
while True:
    for (word, mean) in wordsByDay:
        w = input("What does ' {} ' Mean? : ".format(word))
        if(mean.find(w) != -1):
            print("\t정답")
        else:
            print("\t오답")
            wrongs = wrongs.append((word, mean))
        print(mean)
    print("다시 외우기")
    for w in wrongs:
        print("{} : {}".format(w[0], w[1]))
