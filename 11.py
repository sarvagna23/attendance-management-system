import numpy
import pandas
myarray=numpy.array([[1,2,3],[4,5,6]])
rowname=["a","b"]
colname=["f1","f2","f3"]
mydataframe = pandas.DataFrame(myarray, index = rowname, columns=colname)
print(mydataframe)
