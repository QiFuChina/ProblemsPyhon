def palindrome(list):
# define a method to compare elements where inside list
    for i in range(0, len(list)):
        if list[i] == list[-i-1]:
            result = True
            break
        else:
            result=False
            break   
    # this loop test two elements every times start at begin and end break to execute for loop again.
    # if every times they are equal, it will get true value in this function or get false 
    return result
    # the function obtain a result from here

if __name__=="__main__":
# this command can decide where is the main part to begin script  
# here is a reference form stackoverflow https://stackoverflow.com/questions/419163/what-does-if-name-main-do
    list=input("input elements:")
    # acquire elements from keyboard
    if palindrome(list):
        print("%s is a palindrome" % list)
    else:
        print("%s is not a palindrome" % list)
    # if-else statement judge the value of function palindrome and output differernt result
    # whatever types users input, they all will be converted to string to compare conveninently 