def sumInterval(checklist):
  a=len(checklist)
  length = 0
  count = 0
  ar1=0
  ar2=0
  for i in range (a):
    ar1 = checklist[i][1]
    ar2 = checklist[i][0]
    count = ar1 - ar2
    length = length + count
  return length
    
lista=input("dose mia lista:")
x=sumInterval(lista)
print "to diastima einai: %s" % (x)