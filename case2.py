# transforming data without using in-built functions

import csv
import pandas as pd
import time
start_time = time.time()
df = pd.read_csv("data.csv")
count = df["Name"].count()
with open("Output-case2.csv" , 'w' ,newline= "") as file:
    for i in range(0,count):
        name = df['Name'][i]
        phone = df['Phone No.'][i]
        address = df['Address'][i]
        salary = df['Salary'][i]
        gender = df['Gender'][i]
        list1 = []
        list1.append(name.upper())
        list1.append('+91' + str(phone))
        list1.append(address.upper())
        list1.append(salary + (salary * 0.1))
        if(gender == 'Male'):
            a = 1
        else:
            a = 0
        list1.append(a)
        writer = csv.writer(file)
        writer.writerow(list1)


final_time = time.time()
print(final_time - start_time)