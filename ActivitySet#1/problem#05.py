# Functions

def computepay(h, r):
    

  
   if h > 40:
       n = h * r
       o = (h - 40)* (r * 0.5)
       p = n + o
   else :
       p = h * r
   return p
   

h = float(input("Enter Hours:"))
r = float(input("Enter Rate:"))
pay = computepay(h,r)
print ("Pay",pay)
 

