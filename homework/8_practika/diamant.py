number=int(input('number='))
while not number%2 or number <0:
    number=int(input('positive number'))

for i in range(1,number+1,2):
    print((number-i)//2*' ',i*'*',sep='')
for i in range(number-2,0,-2):
    print((number-i)//2*' ',i*'*',sep='')
