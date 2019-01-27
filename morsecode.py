#!/python3.7

import pickle as p
with open('morse.pkl','rb')as f:
      a=p.load(f)
def init():
      flag=1
      while(flag):
            try:
                  b=input('chose English To MorseCode[1] or MorseCode To Eglish[2]\nplease write 1 or 2:')
                  c=int(b)
                  if c!=1 and c!=2:
                        print('Please chose 1 or 2')
                  else:
                        print('OK')
                        flag=0
            except ValueError:
                  print('Please input 1 or 2')
      return c
def deal(num):
      if num==1:
            En_m=''
            En=input('Please input English sentence(please write lowercase)\n:')
            er=0;
            for letter in En:
                  if letter in a:
                        En_m=En_m+str(a.get(letter))
                  else:
                        En_m=En_m+letter
                        er=er+1
            if er!=0:
                  print(str(er)+' character has no morsecode')
            return En_m
      else:
            Code_e=''
            Code=input('Please input MorseCode("-"is point,"="is line)\n:')
            Co=Code.split(' ')
            x=0
            er=len(Co)
            for l in Co:
                  for letter in 'abcdefghijklmnopqrstuvwxyz1234567890?/|-. ':
                        if l==a[letter].rstrip():
                              Co[x]=letter
                              er=er-1
                              break
                  Code_e=Code_e+Co[x]
                  x=x+1
            if er!=0:
                  print(str(er)+' character has no english word(s)')
            return Code_e
                        

print(deal(init())+'\n("-"is point,"="is line)')
