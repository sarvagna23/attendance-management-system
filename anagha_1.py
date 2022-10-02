def main():
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

    def ceasar_cipher(s,shift):
        cipher=""
        for i in s:
            if i.isupper():
                cipher+=chr((ord(i)+shift-65)%26+65)
            else:
                cipher+=chr((ord(i)+shift-97)%26+97)
        return cipher

    s=input("Enter the string to be encrypted : ")
    shift=int(input("Enter the shift value : "))
    print("The encrypted string is : ",ceasar_cipher(s,shift))

if __name__=="__main__":
    main()
