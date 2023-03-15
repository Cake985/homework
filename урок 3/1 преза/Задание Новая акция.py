a = int(input())
b = int(input())
c = int(input())
if a < b < c:
    print('Акция!')
    print((a+b+c)/2)
elif a > b > c:
    print('Акция!')
    print((a+b+c)/3)
else:
    print('К оплате:')
    print(a+b+c)