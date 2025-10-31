# pandas_investigation.py

import pandas as pd


df = pd.DataFrame({
    'A':[1, 2, 3, 4], 
    'B':[5, 6, 7, 8], 
    'C':[9, 10, 11, 12]
              })

print (df)

print (df['B'])


df = pd.read_json("customers.json")

print (df[['CustomerID', 'CompanyName']])


df_sales = pd.read_json("salesdata.json")

#print (df_sales)

pivot = pd.pivot_table(df_sales, 
                       index="product", 
                       columns="colour", 
                       values="quantity", 
                       aggfunc="sum", 
                       fill_value=0)

pivot['totals'] = pivot.sum(axis=1)

totals_row = pivot.sum(axis=0).to_frame().T

# set the label in the first column of the totals_row
totals_row.index = ["Totals"]


# join the two dataframes together

pivot_with_totals = pd.concat([pivot, totals_row])

print (pivot_with_totals)



#print(pivot)

#print (totals_row)


