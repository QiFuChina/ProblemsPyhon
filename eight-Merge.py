def merge(str):
    # a function to list and sort
    str=str1+str2
    str=list(str)
    # string can not be sorted by using sort function,but it can be changed to list type
    str.sort()
    print(str)

if __name__=="__main__":
    str1=input("input list1:")
    str2=input("input list2:")
    
    merge(str)

#print("list3:%s"%(list3.sort()))