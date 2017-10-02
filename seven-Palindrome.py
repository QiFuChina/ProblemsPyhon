def palindrome(list):
    # define a method to compare elements where inside list
    for i in range(0, len(list)):
        if list[i] == list[-i-1]:
            result = True
            break
        else:
            result=False      
    return result

if __name__=="__main__":
    list=input("input elements:")
    if palindrome(list):
        print("%s is a palindrome" % list)
    else:
        print("%s is not a palindrome" % list)