a = str(input())
b = a.split(' ')
c = b.split(list('.ическая')) or b.split(list('.ический'))
stor = c + '.'
print(stor + b[1::])
