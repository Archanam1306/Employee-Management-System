import pickle
import os
f=open('Employee.dat','wb')
n=int(input('Enter the no.of records:'))
for i in range(n):
    l=[]
    nm=input('Enter name:')
    ag=int(input('Enter age:'))
    dp=input('Enter department:')
    ds=input('Enter designation:')
    sal=int(input('Enter salary:'))
    l.append(nm)
    l.append(ag)
    l.append(dp)
    l.append(ds)
    l.append(sal)
    pickle.dump(l,f)
print(l)
f.close()

ch='y'
while ch=='y':
    print('\n\t\t\tMENU')
    print('\t\t\t*******')
    print('\t\t1.Details of manager earning more than 50000 in finance OR in admin dept.')
    print('\t\t2.Delete employee details who have reached retirement age(58 yrs)')
    print('\t\t3.Exit')
    opt=int(input('Enter your option:'))
    if opt==1:
        f1=open('Employee.dat','rb')
        try:
            while True:
                d=pickle.load(f1)
                if d[3]=='manager' and d[2] in ('finance','admin') and d[4]>50000:
                    print('\t\t',d)
        except EOFError:
            f1.close()
    elif opt==2:
        f2=open('Employee.dat','rb')
        t1=open('Temp.dat','wb')
        print('The inputed details:')
        try:
            while True:
                b=pickle.load(f2)
                print('\t\t',b)
                if b[1]!=58:
                    pickle.dump(b,t1)
        except EOFError:
            f2.close()
            t1.close()
        os.remove('Employee.dat')
        os.rename('Temp.dat','Employee.dat')
        print('\t\tSuccessfully deleted')
        print('The new list:')
        f3=open('Employee.dat','rb')
        try:
            while True:
                v=pickle.load(f3)
                print('\t\t',v)
        except EOFError:
            f3.close()
    else:
        ch=input('Would you like to continue(y/n)?')
        if ch!='y':
            print('\t\tProgram terminated')
            print('\t\t******************')
            break
                    
        
