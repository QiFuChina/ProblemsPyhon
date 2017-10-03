def reverse(str):
# a function to reverse a string
    str=list(str)
    # string can not be reversed by using reverse function,but it can be changed to list type
    str.reverse()
    print(str)

if __name__=="__main__":
    str=input("input:")
    reverse(str)
    # call reverse function and print it
   