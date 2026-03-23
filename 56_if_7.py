# write a program to findout which is cheaper approach to buy IPhone 17 pro max.  consider use is going usa should he buy iphone from usa or from india.
'''
1  accept indian rupees price 
2  accept usa price 
3  accept dollar rate
4  calculate price of mobile in indian rupees 
   price2 = usa_price * dollar 
5  compare indian price with price2(price of iphone in usa in indian rupees)
'''
india_price = int(input("enter price"))
usa_price = int(input("enter price"))
dollar = int(input("enter rate"))
price2 = usa_price * dollar
print(price2)

if india_price>0:
    print(f"price of {india_price}")

if price2>0:
    print(f"price of {price2}")   











    

