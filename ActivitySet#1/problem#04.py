# Conditional Execution
hrs = float(input("Enter Hours:"))
rate = float(input("enter rate:"))
pay = hrs * rate
if  hrs > 40 :
    r = hrs * rate
    o = (hrs - 40) * (rate * 0.5)
    pay = r + o
    


else :
    pay = hrs * rate

print("pay",pay)

    
    








