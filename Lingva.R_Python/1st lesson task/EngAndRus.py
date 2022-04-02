import sys
n = input()
b = input()
true1 = 0
true2 = 0
true3 = 0
true4 = 0

for i in range (len(n)):
    if "0"<=n[i]<="9":
        sys.exit ("Wrong input")
    else:
        if "a"<=n[i]<="z" or "A" <= n[i]<="Z":
            true1+=1
        elif "а"<=n[i]<="я" or "А" <= n[i]<="Я":
            true2+=1

for i in range (len(b)):
    if "0"<=b[i]<="9":
        sys.exit ("Wrong input")
    else:
        if "a"<=b[i]<="z" or "A" <= b[i]<="Z":
            true3+=1
        elif "а"<=b[i]<="я" or "А" <= b[i]<="Я":
            true4+=1


if true1 == len (n) and true4 == len(b):
    print ("Eng is", n)
    print ("Rus is", b)
elif true2 == len (n) and true3 == len (b):
    
    print ("Eng is", b)
    print ("Rus is", n)
else:
    print ("Wrong")
