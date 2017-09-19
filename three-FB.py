# FizzBuzz
# reference: http://wiki.c2.com/?FizzBuzzTest


for x in range(1,100):
    s=""
    if (x%3==0 and x%5==0):
        s+="FizzBuzz"
    # This statment decides next statment whether should be excuted.If this is true that will skip next two else if and one else statment then print it.
    elif x%3==0:
        s+="Fizz"
   
    elif x%5==0:
        s+="Buzz" 
    # If one of them is right,s will get a different string and print
    else:
        s=x
    # If all if and else statment are false,it will execute that give s a number value and print finally
    print (s)