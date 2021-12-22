print('Welcome to the conversion zone.\nHere you can convert INR to any currency you want to.')

with open("currencyfile.txt") as f:
    text = f.readlines()

Dictconvert= {}
for line in text:
    parse= line.split("\t")
    Dictconvert[parse[0]]=parse[1]

val=float(input('Enter the value: '))
print('The currency name to which u can convert are given below:\n')
[print(items) for items in Dictconvert.keys()]
currencyIs=input("Enter the name of currency: ")
print(f'{val} INR is equals {val*float(Dictconvert[currencyIs])} {currencyIs}')
print('Thanks!Do visit our site again.')