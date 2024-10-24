n = int(input("値段を入力してください: "))
p = int(input("投入金額を入力してください: "))

list = [500, 100, 50, 10]

oturi = p - n
print('おつり{}円\n'.format(oturi))
for i in list:
    money = oturi // i
    oturi = oturi % i
    print('{}円玉: {}枚'.format(i, money))
