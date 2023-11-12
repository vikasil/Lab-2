import csv
from random import randint
with open('books.csv', newline='') as File:  
    reader = csv.reader(File)
    print("task1")
    i=0
    kol=0
    for row in reader:
        row=str(row)
        i+=1
        if i>1:
            nazv=row.split(";")[1]
            if len(nazv)>30:
                #print(nazv,len(nazv))
                kol+=1
print(kol)

print("task2")
print("Введите автора")
avtor=input()
with open('books.csv', newline='') as File:  
    reader = csv.reader(File )
    for row in reader:
        row=str(row)
        #print(row.split(";")[3])
        i+=1
        if i>1:
            if (row.split(";")[3]==avtor) and (float(row.split(";")[7])>=150.0):
                print(row.split(";")[1])
                
print("task3")
with open('books.csv', newline='') as File:
    reader = list(csv.DictReader(File, delimiter=';'))
    bibl = open("bibliograf.txt", "w")
    for i in range( 20):    
        number = randint(1, 9400)
        bibl.write(f"{i+1} {reader[number]['Автор']} - {reader[number]['Название']} - год \n") #в таблице нет дат
