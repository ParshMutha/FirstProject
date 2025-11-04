import pandas as pd 
import numpy as np
a = pd.Series([1,2,3,4,5],index= ['a','b','c','d','e'])
print(a)
b = pd.Series(np.random.randn(5),index= ['a','b','c','d','e'] )
print(b)

data = pd.Series({'a':10,'b':20,'c':30}, )
print(type(data))
df = pd.DataFrame(data)
print(df)
data2 = {"Name : ['Alice', 'Bob', 'Charlie'], Marks : [10,89,78]"}
p = pd.DataFrame(data2)
