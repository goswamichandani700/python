import currency

dollar = int(input("enter dollar"))
euro = int(input("enter euro"))
yen = int(input("enter yen"))
pound = int(input("enter pound"))

print('dollar',currency.dollartorupees(dollar))
print('euro',currency.eurotorupees(euro))
print('yen',currency.yentorupees(yen))
print('pound',currency.poundtorupees(pound))