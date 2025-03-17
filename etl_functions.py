import pandas as pd


'''The following function counts the number of empty and null values
in a pandas series. (Supports the functions below: missing_values_diag and general_information).'''

def missing_values(c):
  empty_spaces=c.apply(lambda x:x=="").sum()
  spaces=c.apply(lambda x:x==" ").sum()
  none_values=c.apply(lambda x: x==None).sum()
  nan_values=c.isna().sum()
  return empty_spaces+spaces+none_values+nan_values

'''The following function takes as input a dataframe and a column name and returns
the percentage of missing values and a category that is assigned to such column according
to such percentage'''

def missing_vals_diag(data,col):
   missing_count=missing_values(data[col])
   missing_values_per=round(missing_count/len(data),2)
   if missing_values_per<=0.30:
      print(f'The percentage of missing values in the column {col} is:{missing_values_per}, (Low)')
   elif missing_values_per>0.30 and missing_values_per<=0.60:
      print(f'The percentage of missing values in the column {col} is:{missing_values_per}, (Moderate)')
   else:
      print(f'The percentage of missing values in the column {col} is: {missing_values_per}, (High)')

'''The following function takes a dataframe as input and 
for each column it gets: the datatype, the
null values count and the percentage of null values.'''

def general_information(data):
    columns=[column for column in data.columns]
    dtypes=[type(column) for column in data.columns]
    missing_values_count=[missing_values(data[column]) for column in data.columns]
    missing_values_percentage=[round(i/len(data),2) for i in missing_values_count]
    return pd.DataFrame({"column":columns,"data_type":dtypes,"missing_values":missing_values_count,"missing_values_percentage":missing_values_percentage})