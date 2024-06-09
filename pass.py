

import random
import string
l=int(input("enter password length:"))
low=string.ascii_lowercase
up=string.ascii_uppercase
no=string.digits
sc=string.punctuation
total=low + up + no + sc
P=random.sample(total,l)
Password="".join(P)
print(Password)
