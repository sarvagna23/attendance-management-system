print('''
if u want to convert decimal into
binary ( then type ) - 2
octal                - 8
hex                  - 16
''')
e=int(input('ENTER CODE :'))
n=int(input('enter decimal part only of decimal number (eg- 978):'))
p=int(input('enter precision :'))
d=len(str(n))
for i in range(p):
    n=n*e
    if n>(10**(d)):
        print(n//10**d,end='')
        n=n%10**d
    else :
        print(0,end='')

input()
