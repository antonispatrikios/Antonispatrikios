import math
firstar=[]
p= 0
q= 0
i= 0
found=False
a=int(input("Dose ena arithmo megalitero toy 2 :"))
while a<2:
  a=int(input("O arithmos pou dosate einai mikroteros tou 2. dose ena kainourio arithmo :"))
b=int(input("Dose ena megalitero arithmo :"))
while b<=a:
  b=int(input("O arithmos pou dosate einai mikroteros apo ton proto arithmo. dose ena kainourio arithmo:"))
d=int(input("dose ena tixeo akereo:"))
for i in range(a,b+1):
  if i > 1:
    for j in range(2,i):
      if (i % j) == 0:
        break;
      else:
        firstar.append(i)
        
print firstar
while i < (len(firstar) - 1) and found == False:
  if abs(firstar[i]-firstar[i+1])==d:
    p=i
    q=i+1
    flag=True
  i+=1
if p==0 and q==0:
  print "Kanena apotelesma!"
else:
  print firstar[i] 
  print firstar[i+1]