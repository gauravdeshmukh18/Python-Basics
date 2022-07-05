##Sum of all natural numbers 1 to n
a = input("Enter the number:")
x = 0
for i in xrange(1,a+1):
    x =x+i
print x


2...####Sum of all Even Numbers natural
a = input("Enter the number:")
b = 0
c = ('')
for x in xrange(0,a+1):
    if x % 2 == 0:
        b = b+x
        print(x)
print c
print b

3...####Sum of all Odd Numbers Natural
a =input("Enter the number:")
b = 0
c = ''
for x in xrange(0,a+1):
    if x % 2-1 == 0:
        b = b+x
        print(x)
print c
print b


4...####Multiplication
a = input("Enter the number:")
b = input("Enter the number:")
c = a*b
print c


5...####To Count the number of digits in a number (with 2 examples)
a = int(input("Enter the number:"))
for x in xrange(1,15):
    b = a*x
    print(a,'*',x,'=',b)


a = int(input("Enter the number:"))
for x in xrange(1,10):
    c = a*x
    print(a,'*',x,'=',c)
