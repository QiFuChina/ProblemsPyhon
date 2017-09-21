import math
# import math method to calculeate value directly
fact=str(math.factorial(100))
print("factorial is "+fact)
# get value and show it as string type
resultat=0
for i in fact:
    resultat +=int(i)
    # set a integer to get sum of every numbers from value of factorial  
resultat=str(resultat)
print("sum of digits is "+resultat)
# change resultat type to display it as string 