fruits=["strawberry",'apple',"blueberry","raspberry","mango","blackberry","orange","kiwi","watermelon","dragon fruit"]
print("Index of mango = ",fruits.index("mango"))

print("length of the array fruits =",len(fruits))

fruits.pop(0)
print("after removing index 0 =",fruits)

fruits.insert(0,"orange")
print("after inserting orange =",fruits)

fruits.reverse()
print("After reversing the array =",fruits)
fruits.clear()
print("after clearing whole array =",fruits)
