def is_prime(t):
    if t in (1,2,3):
        return True

    for i in range(2,round(t**0.5)+2):
        if not t%i:
            return False

    return True
t=int(input())
print(is_prime(t))
sq=lambda x: x**2
numbers=[i for i in range(1,51)]
num1=[]
for i in numbers:
    if is_prime(i):
      num1.append(sq(i))
print(list(map(int,num1)))
