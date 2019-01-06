import random
import time
y=input('all:')
x=input('max:')
a=y%(x+1)
z = random.randint(0,1)
print('random------(please wait a minute)')
time.sleep(2)
#print z
#print a
c=1
b=0
if z==1:
    print('I go')
    if a==0:
        d=(x/2)+a
        print(d)
        while c < 100:
            b=input('number:')
            if b<=d or b>=(d+x+1):
                print('\033[35merror\033[37m.')
            else:
                if b==(x+1)*c:
                    if b==y :
                        print('\033[32myou are win\033[37m.')
                        break
                    elif b>y:
                        print('\033[35merror\033[37m.')
                    else:
                        d=(x/2)+b
                        time.sleep(1)
                        print d
                        c=c+1
                else:
                    if b>y:
                        print('\033[35merror\033[37m.')
                        continue
                    d=(x+1)*c
                    time.sleep(1)
                    print d
                    if d==y:
                        print('\033[33myou are fail\033[37m.')
                        break
                    c=c+1
    else:  
        print  (a+(x+1)*(c-1)) 
        while c < 100 :
            b=input ('number:')
            if b >= a+(int(x)+1)*c or b <= a+(int(x)+1)*(c-1) :
                print('\033[35merror\033[37m.')
            else :
                time.sleep(1)
                print(a+(x+1)*c)
                c = c+1
            if (a+(x+1)*(c-1)) == int(y):
                print('\033[33myou are fail\033[37m.')
                break
else:
    print('you go')
    if a==0:
        while c < 100 :
            b=input('number:') 
            if b >= a+(int(x)+1)*c or b <= a+(int(x)+1)*(c-1) :
                print('\033[35merror\033[37m.')
            else :
                time.sleep(1)
                print(a+(x+1)*c)
                c = c+1
            if (a+(x+1)*(c-1)) == int(y):
                print('\033[33myou are fail\033[37m.')
                break  
    else:
        d=0
        while c<100:
            b=input('number:')
            if b<=d or b>=(d+x+1):
                print('\033[35merror\033[37m.')
            else:
                if b==a+(x+1)*(c-1):
                    if b==y :
                        print('\033[32myou are win\033[37m.')
                        break
                    else:
                        d=x/2+b
                        time.sleep(1)
                        print(d)
                        c=c+1
                else:
                    if b>y:
                        print('\033[35merror\033[37m.')
                        continue
                    if b<a+(x+1)*(c-1) :
                        d=a+(x+1)*(c-1)
                        time.sleep(1)
                        print d
                    else: 
                        d=a+(x+1)*c
                        time.sleep(1)
                        print d
                        c=c+1
                    if d == y:
                        print('\033[33myou are fail\033[37m.')
                        break
