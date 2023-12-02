# Pandas

# Series

# Creation of series

# By using list

S = pd.Series([1,2,3,4,5])
print(S)

S1 = pd.Series([1,2,3,4,5,6],index = [1,2,3,4,5,6])
print(S1)
print()

# From Dictionary

S2 = pd.Series({'Punjab':'Chandigarh','Gujrat':'Ahemdabad','Maharasthra':'Mumbai'})
print(S2)
print()

# From nd array

S3 = pd.Series(np.array([1,2,3,4]))
print(S3)
print()

S4 = pd.Series(np.linspace(1,10,5))
print(S)
print()

S5 = pd.Series(np.arange(1,15))
print(S5)
print()

# Renaming the indices

S5.index = range(1,15)
print(S5)

# Giving  label

S5.name = 'Integers'
print(S5)

S5.index.name = 'Integers'
print(S5)

print(S5.dtype)
print()


# Accessing The values

L = ['Apple','Mango','Orange','Banana','Cherry']

S = pd.Series(L,index = ['F1','F2','F3','F4','F5'])
print(S)
print()

print(S.iloc[[0,1,2]])                               # Using iloc attribute for accessing values
print()

print(S.loc['F1':'F5'])                              # Using loc attribute for accessing values
print()



# Datafrmes - It is a 2D arrangement of elements in the form of rows and columns

# Ways to create a dataframe

# From list

L1 = [[12,23,45,56],[14,56,78,67]]

df = pd.DataFrame(L1)
print(df)
print()

# From  array

ar = np.array([[12,34,55],[56,34,23],[12,45,87]])

df = pd.DataFrame(ar)
print(df)

# From tuple

t = ((1,2,3,4,5),(2,34,5,6,7))

df1 = pd.DataFrame(t)
print(df1)
print()

# From Series

S = pd.Series(['Monday','Tuesday','Wednesday'])

Df = pd.DataFrame(S)
print(Df)
print()

# From Dictionary

Dict = {'Roll no':[1,2,3,4],'Name':['Raj','Roy','Sam','Mike'],'Marks':[34,37,40,39]}

df1 = pd.DataFrame(Dict)
print(df1)
print()

# Change of indexes and column labels

Dict = {'Roll no':[1,2,3,4],'Name':['Raj','Roy','Sam','Mike'],'Marks':[34,37,40,39]}

df2 = pd.DataFrame(Dict,index = [1,2,3,4])
print(df2)
print()

df = pd.DataFrame([[1,2,3,4],[5,6,7,8],[9,10,11,12]])

df.index = range(1,4)
df.columns = ['A','B','C','D']

print(df)
print()

# Accessing of values

df = pd.DataFrame([[1,2,3,4],[5,6,7,8],[9,10,11,12]])


print(df[1][1])
print()
print(df[1:][:2])
print()
print(df.loc[0:2])
print()
print(df.iloc[::-1])

# Various Attributes of dataframes
Dict = {'Roll no':[1,2,3,4],'Name':['Raj','Roy','Sam','Mike'],'Marks':[34,37,40,39]}
df = pd.DataFrame(Dict,index = [1,2,3,4])


print(df.index)                       # It gives the index positions
print()

print(df.columns)                     # It gives the column values
print()

print(df.shape)                       # It gives the shape
print()

print(df.dtypes)                      # It gives the datatype
print()

print(df.describe)                    # It gives the Description
print()

print(df.head(2))                     # It gives the First 2 rows
print()

print(df.tail(1))                     # It gives the last 1 row
print()

print(df.size)                        # It gives the number of elements
print()

# Math functions

print(df.max)                         # It gives the maximum value
print()

print(df.min)                         # It gives the minimum value
print()

print(df.sum(axis=1))                 # It gives the Sum of the rows
print()

print(df.mean())                      # It gives the Mean value
print()

print(df.median())                    # It gives the median value
print()

print(df.sum(0))                      # It gives the Sum of columns
print()

# Deleting a row
df = df.drop(1)
print(df)
print()

# Deleting a column
df = df.drop(['Name'],axis = 1)
print(df)


# Converting Csv file into a dataframe

df = pd.read_csv('new_sample.csv')
print(df)