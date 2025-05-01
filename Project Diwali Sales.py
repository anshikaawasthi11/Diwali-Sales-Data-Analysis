import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# Try with a more compatible encoding
file_path = r"D:\Anshika\Vs Code\Diwali Sales Data.csv"
df = pd.read_csv(file_path, encoding='latin1')
(df.shape)
(df.info())
# DATA CLEANING 
#Dropping the column 
(df.drop(['Status', 'unnamed1'], axis=1, inplace=True))
print(df.info())
# Checking null values
(pd.isnull(df).sum()) 
# To Drop null Values
(df.dropna(inplace= True)) # inplace is used for Saving the Change in that line of code
print(df.shape)
print(pd.isnull(df).sum())
# Changing the dataype
df['Amount'] = df['Amount'].astype('int')
print(df['Amount'].dtypes)
print(df.info())
# Rennaming the column
(df.columns) # for seeing all the columns of the data
df1=df.rename(columns={'Marital_Status':'Marriage'})
print(df1.columns)
#EDA

#Gender(EDA)
ax= sns.countplot(x ='Gender',data = df) #x= X axis and the count is y axis
for bars in ax.containers: # containers (used for showing the values)
    ax.bar_label(bars)
(plt.show()) # (according to the bar chart female has made more purchases)
sales=(df.groupby(['Gender'],as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False)) # For showing the sum of amount of male and female
a= sns.barplot(x='Gender',y='Amount',data =sales)
plt.show() # from the above graphs we can see that most of the buyers are females and the most of the purchases are also made by them

#Age(EDA)
b= sns.countplot(x ='Age Group',data = df, hue= 'Gender')
for bars in ax.containers: # containers (used for showing the values)
    ax.bar_label(bars)
print(plt.show())
# Total Amount vs Age Group
sales_age=(df.groupby(['Age Group'],as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False)) # For showing the sum of amount of male and female
a= sns.barplot(x='Age Group',y='Amount',data =sales_age)
plt.show() # according to this chart most of the buyers are of age group between 26-35 yrs female and has spent more amt

#State (EDA)
b= sns.countplot(x ='Gender',data = df, hue= 'State')
for bars in ax.containers: # containers (used for showing the values)
    ax.bar_label(bars)
print(plt.show())
# Total number of orders from top 10 states
sales_state = (
    df.groupby(['State'], as_index=False)['Orders']
    .sum()
    .sort_values(by='Orders', ascending=False)
    .head(10)
)
sns.set(rc={'figure.figsize': (15.5, 8)})  # Added height as well
sns.barplot(x='State', y='Orders', data=sales_state)
plt.show() # according to the graph Uttar Pradesh, Maharashtra, Karnataka are top states which have the max orders
# Total amt/Sales from top 10 states
sales_state = (
    df.groupby(['State'], as_index=False)['Amount']
    .sum()
    .sort_values(by='Amount', ascending=False)
    .head(10)
)
sns.set(rc={'figure.figsize': (15.5, 8)})  # Added height as well
sns.barplot(x='State', y='Amount', data=sales_state)
plt.show() # according to the graph most of the orders are from UP, Maharashtra, Karnataka with max purchasing power 

# Marriage/ Marital Status (EDA)
b = sns.countplot(x='Marriage', data=df1)  # Use actual column name
sns.set(rc={'figure.figsize': (6, 5)})
for bars in b.containers:
    b.bar_label(bars)
plt.show() # according to the graph most purchases were made by married people

#Occupation (EDA)
sns.set(rc={'figure.figsize': (20, 5)})
ax = sns.countplot(data= df,x= 'Occupation')
for bars in ax.containers:
    ax.bar_label(bars)
plt.tight_layout()
print(plt.show()) # according to the graph most of the buyers are working in It, Aviation and healthcare centre
#Having the most purchasing power
sales_state = (
    df.groupby(['Occupation'], as_index=False)['Amount']
    .sum()
    .sort_values(by='Amount', ascending=False))
sns.set(rc={'figure.figsize': (20, 5)})
sns.barplot(data=sales_state,x='Occupation',y='Amount')
plt.show()#according to the graph most of the buyer are from IT,Aviation,Healthcare sector

#Product Category(EDA)
sns.set(rc={'figure.figsize': (20, 5)})
ax = sns.countplot(data= df,x= 'Product_Category')
for bars in ax.containers:
    ax.bar_label(bars)
plt.xticks(rotation=45)
plt.tight_layout()
print(plt.show()) # according to the graph the most orders were made for Clothing,food,electronic gadgets
# total amount (group by Product category)
sales_state = (
    df.groupby(['Product_Category'], as_index=False)['Amount']
    .sum()
    .sort_values(by='Amount', ascending=False))
sns.set(rc={'figure.figsize': (20, 5)})
sns.barplot(data=sales_state,x='Product_Category',y='Amount')
plt.show() # most of the product sold from food,clothing and electronic gadget category

#CONCLUSION: Married women between age group of 26-35 from UP,Maharashtra and Karnataka working in IT,Aviation and Healthcare Dept are more likely to buy products from Food,Clothing and electronic gadgets.







