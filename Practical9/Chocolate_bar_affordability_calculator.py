def Chocolate_bar_affordability_calculator(x,y):
    z=int(y)//int(x)
    print('the number of bars that can be bought:'+str(z))
    w=int(y)%int(x)
    print('the change that will be left over:'+str(w))
    return z

total_money=input('Your total money:')
price=input('One chocolate bar price:')
x=price
y=total_money
a=Chocolate_bar_affordability_calculator(x,y)