fname = input("Enter file name: ")
fh = open(fname)
lst = list()
x = fh.read()
words = x.split()
for n in words:
    if n not in lst:
        lst.append(n)
lst.sort()
print(lst)
  
