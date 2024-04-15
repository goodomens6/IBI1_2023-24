def favourite_James_Bond(x):
    y=int(x)+18
    if y>=1973 and y<=1986:
        z='Roger Moore'
    elif y>=1987 and y<=1994:
        z='Timothy Dalton'
    elif y>=1995 and y<=2005:
        z='Pierce Brosnan'
    elif y>=2006 and y<=2023:
        z='Daniel	Craig'
    else:
        z='None'
    return z

x=input("Your born year:")
w=favourite_James_Bond(x)
print(w)