# creating data for all the three test cases
import csv
import random
import pandas as pd
# number of input rows you want to create

n = 500000


df = pd.read_excel("cities.xls",sheet_name="sheet1")
cities = df['Name of City'].tolist()
df1 = pd.read_excel("names.xlsx", sheet_name="Sheet1")
names = df1['Name'].tolist()
gender = ["Male","Female"]
with open("data.csv",'w',newline = "")as file:
    writer = csv.writer(file)
    writer.writerow(['Name','Phone No.','Address','Salary','Gender'])
    for i in range(1,n):
        writer.writerow([random.choice(names),random.randint(1000000000,9999999999),random.choice(cities),random.randint(100000,1000000),random.choice(gender)])