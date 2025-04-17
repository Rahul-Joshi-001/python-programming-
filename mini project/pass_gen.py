import random
import string

val = string.ascii_letters + string.digits

n = int(input("Enter the length of password"))

passw =  ""
for i in range(0,n):
    passw += random.choice(val)

print(passw)