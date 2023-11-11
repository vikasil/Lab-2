import csv
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