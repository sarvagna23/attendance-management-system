import numpy
import pandas
myarray=numpy.array([[1,2,3],[4,5,6]])
rowname=["a","b"]
colname=["f1","f2","f3"]
mydataframe = pandas.DataFrame(myarray, index = rowname, columns=colname)
print(mydataframe)




# Python Program to calculate the square root

# Note: change this value for a different result
num = 8 

# To take the input from the user
#num = float(input('Enter a number: '))

num_sqrt = num ** 0.5
print('The square root of %0.3f is %0.3f'%(num ,num_sqrt))
