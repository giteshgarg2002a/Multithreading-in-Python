''' In the below program a csv file is extracted and
converted to multiple small files and changes are done in the
file and loaded / combined in a new csv file using multithreading'''
''' Using Multithreading three operations are performed 
Extract , Transform and Load'''

#inporting libraries
import pandas as pd
import threading
import csv
import time

#function to declare start time of the process
start_time = time.time()
list_dataframes = []
new_dataframes = []
output_files = []

# Name of csv file containing data to be changed
input_csv = 'data.csv'

# code for splitting the file into multiple files
number_lines = sum(1 for row in (open(input_csv)))

#defining number of rows each file contains
rowsize = 100000
count = 0

#list containing names of splitted files
list_of_files = []
for i in range(1,number_lines,rowsize):
    df = pd.read_csv(input_csv,
          header = None,
          nrows = rowsize,
          skiprows = i)
    out_csv = 'case3input' + str(count) + '.csv'
    with open(out_csv,'w',newline= "") as file:
        writer = csv.writer(file)
        writer.writerow(['Name', 'Phone No.', 'Address', 'Salary', 'Gender'])
    df.to_csv(out_csv,
          index=False,
          header=False,
          mode='a',
          chunksize=rowsize)
    count = count + 1
    list_of_files.append(out_csv)


number_of_files = len(list_of_files)
def extract(x):
    df = pd.read_csv(list_of_files[x])
    list_dataframes.append(df)

def transform(x):
    df = list_dataframes[x]
    df['Name'] = df["Name"].str.upper()
    df['Phone No.'] = '+91' + df['Phone No.'].astype(str)
    df['Address'] = df["Address"].str.upper()
    df['Salary'] = df["Salary"] + (0.10 * df["Salary"])
    df_gender = pd.get_dummies(df['Gender'], drop_first=True)
    df = pd.concat([df.drop(['Gender'], axis=1), df_gender], axis=1)
    df.columns = ['Name', 'Phone No.', 'Address', 'Salary', 'Gender']
    output_csv = "Case3Output" + str(x) + ".csv"
    df.to_csv(output_csv,index = False)
    output_files.append(output_csv)

def load(x):
    print(x)
    combined_csv = pd.concat([pd.read_csv(f)for f in output_files])
    combined_csv.to_csv("final_data.csv", index=False)

# creating threads and
l1 = threading.Thread(target=extract , args= (0,))
l1.start()
l1.join()
l2 = threading.Thread(target=transform , args= (0,))
l2.start()
l3 = threading.Thread(target=extract , args= (1,))
l3.start()
l2.join()
l3.join()

if(number_of_files>2):
    for i in range(0,number_of_files-2):
        l1 = threading.Thread(target=load , args= (i,))
        l2 = threading.Thread(target=transform, args=(i+1,))
        l3 = threading.Thread(target=extract, args=(i+2,))
        l1.start()
        l2.start()
        l3.start()
        l1.join()
        l2.join()
        l3.join()

l1 = threading.Thread(target=load , args= (number_of_files-2,))
l1.start()
l1.join()
l2 = threading.Thread(target=transform , args= (number_of_files-1,))
l2.start()
l3 = threading.Thread(target=load , args= (number_of_files-1,))
l3.start()
l2.join()
l3.join()



final_time = time.time()
print(final_time - start_time)
