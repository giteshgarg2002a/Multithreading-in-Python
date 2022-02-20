# transforming data using pandas
import pandas as pd
import time

#in case 1 we have converted
# the name of the person in upper case
# phone number as string type
# address as upper case
# increment in salary of 10 percent
# creating dummies for gender automatically like in this case 1 for male and 0 for female


start_time =time.time()
df = pd.read_csv('data.csv')
df['Name']= df["Name"].str.upper()
df['Phone No.'] = '+91'+df['Phone No.'].astype(str)
df['Address'] = df["Address"].str.upper()
df['Salary'] = df["Salary"] + (0.10 * df["Salary"])
df_gender = pd.get_dummies(df['Gender'], drop_first=True)
df = pd.concat([df.drop(['Gender'], axis=1), df_gender], axis=1)
df.columns = ['Name','PhoneNo','Address','salary','Gender']
df.to_csv('output-case1.csv', index=False)
final_time = time.time()
print(final_time-start_time)
