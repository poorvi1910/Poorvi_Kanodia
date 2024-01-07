#Q1
'''
for x in range(11):
    for y in range(11):
        for z in range(11):
            if x+y+z==10:
                print('x=',x,'y=',y,'z=',z)
'''

#Q2
'''
l=[]
for i in range(5):
    n=input("Enter name: ")
    l1=n.split()
    n=l1[0].upper()
    for i in l1[1::]:
        n+=i.lower()
    n=n[:len(n)-2:]
    l.append(n)
    l.sort()
for i in range(len(l)):
    print(i+1,'. ',l[i])
'''
                
#Q3
'''
n1=int(input('Enter numer 1: '))
n2=int(input('Enter numer 2: '))
n=input('add/sub/mul/div/mod/exp  : ')
if n.lower()=='add':
    print(n1+n2)
if n.lower()=='sub':
    print(n1-n2)    
if n.lower()=='mul':
    print(n1*n2)
if n.lower()=='div':
    print(n1/n2)
if n.lower()=='mod':
    print(n1%n2)
if n.lower()=='exp':
    print(n1**n2)
'''
              
#Q4
'''
l=int(input("Enter lower limit: "))
u=int(input("Enter upper limit: "))
for i in range(l,u+1):
      for j in range(2,int(i**0.5+1)+1):
          if i%j==0 and i!=j and i!=1:
              break
      else:
          print(i,end =' ')
'''
                
#Q5
'''
l1=[];l2=[];l=[];d={}
for i in range(5):
    n=input('enter name: ')
    l1.append(n)
for i in range(5):
    n=int(input('enter number: '))
    l2.append(n)
for i in range(5):
    l.append([l1[i],l2[i]])
for i in l:
    d[i[0]]=i[1]
sorted_d = dict(sorted(d.items(), key=lambda item: item[1]))
print(sorted_d)
'''
