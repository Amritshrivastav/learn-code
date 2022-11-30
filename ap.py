last_number=int(input("no of sums"))
a=0
b=1
sums=0
while sums<last_number:
   print(a)
   nth=a+b
   a=b
   b=nth
   sums+=1

firstsum=int(input("enter first the no ap series"))
commondifference=int(input(" common difference"))
totalterms=int(input("total terms"))
currentvalue=firstsum
for i in range(0,totalterms):
   print(currentvalue,end=' ')
   currentvalue=currentvalue+commondifference
