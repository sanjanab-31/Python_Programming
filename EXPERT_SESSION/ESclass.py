class supermarket:
    pname=input("Enter product:")
    qty=int(input("Enter quantity:"))
    price=int(input("Enter price:"))

s=supermarket()
print("Product name:",s.pname)
print("Quantity:",s.qty)
print("Price:",s.price)
print("Total price:",s.qty*s.price)