import pandas as pd
import csv

file1='C:/Users/a2z/Downloads/c-127-hw--main/c-127-hw--main/bright_stars.csv'
file2='C:/Users/a2z/Downloads/c-127-hw--main/c-127-hw--main/dwarf_stars .csv'
d1=[]
d2=[]
with open(file1,'r' ,encoding='utf-8')as f:
    reader=csv.reader(f)
    for i in reader:
        d1.append(i)

with open(file2,'r' ,encoding='utf-8')as g:
    reader=csv.reader(g)
    for i in reader:
        d2.append(i)

h1=d1[0]
#print(h1)
h2=d2[0]
h=h1+h2
p_d1=d1[1:]
p_d2=d2[1:]
p_d=[]
for i in p_d1:
    p_d.append(i)
for i in p_d2:
    p_d.append(i)
with open('total_stars.csv','w',encoding='utf-8')as f:
    csv_writer=csv.writer(f)
    csv_writer.writerow(h)
    csv_writer.writerows(p_d)
df=pd.read_csv('total_stars.csv')

