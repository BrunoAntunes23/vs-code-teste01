import random as rd
x=rd.randint(0,100)
p=0
tentativas=0
while p!=x:
   #print(x)
   print(f'total de tentativas : {tentativas}')
   p=int(input("insira seu palpite do numero secreto"))
   if p==x:
       print("parabens voçê acertou ;) \n com um total de {} tentativas ".format(tentativas))
   else:
       print("tente de novo :(\n")
       tentativas=tentativas+1
   