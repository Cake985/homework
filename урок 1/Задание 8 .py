# = трёхзначное число
a = int(input())
b = a % 10
a = a//10
c = a%10
a = a//10
print(b+c+a)