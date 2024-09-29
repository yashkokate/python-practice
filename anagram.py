def anagram(str1,str2):
    str1=str1.lower()
    str2=str2.lower()
    if len(str1)!=len(str2):
        print(str1,str2," are not anagram")
    else:
        sorted_list1=sorted(str1)
        sorted_list2=sorted(str2)
        if sorted_list1==sorted_list2:
            print(str1,str2," are  anagram")
        else:
            print(str1,str2,"are not anagram")

str1=input("Enter stirng1")
str2=input("Enter string2")
anagram(str1,str2)
       