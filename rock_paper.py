# the rock paper sizzer game played with the computuer
from datetime import datetime
import random
x=datetime.now()
print(x)
rock=0
paper=1
sissor=2
print(f"rock={rock},paper={paper},sissor={sissor}")
b=int(input('enter ur opinion'))
a=random.randint(0,2)
print(a)
if a<b:
    print('user win')
elif a>b:
    print('system wins')
else:
    print('tie')