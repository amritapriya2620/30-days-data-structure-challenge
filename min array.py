n=int(input("enter number of element"))
smallest=float('inf')
for i in range(n):
  num=int(input("enter number"))
  if num <smallest:
        smallest=num

print(smallest)       
