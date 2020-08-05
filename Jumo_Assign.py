
import sys

import pandas as pd


inFile = sys.argv[1]
output = sys.argv[2]


# Loading Data from input file argument

loans=pd.read_csv(inFile, error_bad_lines=False, header='infer')

# Creating Month Column with String (I assume all test data in same format) else we need to create in to_date format

loans['Month']=loans.Date.str[4:7]

# Agrregrating Data as per functinality

AgrregationDF = loans.groupby(['Product', 'Network', 'Month']).agg({'Amount': ['sum', 'count']})

# Renaming Aggregation column Names 

AgrregationDF.columns = ['Amounts', 'Counts']

AgrregationDF = AgrregationDF.reset_index()

# Creating Tuple of Aggregations 

AgrregationDF['tuple_agg'] = AgrregationDF.apply(lambda x: (x.Amounts,x.Counts), axis=1)
#AgrregationDF['tuple_agg'] = list(zip(AgrregationDF.Amounts, AgrregationDF.Counts))

# Selecting Headers 

headers = ['Network', 'Product', 'Month', 'tuple_agg']

# Saving output with Sorting and Headers for csv

#AgrregationDF.to_csv('Output/output.csv', columns = headers, index=False)


AgrregationDF.sort_values(['Month','Network'], ascending = True).to_csv(output, columns = headers, index=False)

## Printing Information of arguments

print ("This is the name of the script: ", sys.argv[0])
print ("Input Argument:", sys.argv[1])
print ("Output Location is: ", sys.argv[2])


# Python3  /home/ssr/Desktop/Jumo/Input/Loans.csv /home/ssr/Desktop/Jumo/Output/output.csv