
import pandas as pd
#series
s=pd.Series([10,20,30], index=['a','b','c'])
print(s)

#dataframe
data={
    'Name':['Sarah','Irene','Madrine'],
    'Age':['23','56','35'],
    'City':['Jinja','Gulu','Arua'],
    'Profession':['Engineer','Accountant','Doctor']
}
df=pd.DataFrame(data)
print(df)

#load dataset
df=pd.read_csv('E:\school\courses\mydataset.csv')
print(df)

print(df.head())
print(df.tail())
data_shape=df.shape
print(data_shape)

#print(df.isnull().sum)     #check missing values
#print(df.dropna(inplace=True))  #drop rows with Nan
#print(df.fillna(0,inplace=True))  #fill Nan with 0

#print(df.duplicated().sum())
#print(df.drop_duplicates(inplace=True))



