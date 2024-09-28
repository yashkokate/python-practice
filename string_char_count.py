def count_char_string(user_string):
    no_spaces=user_string.replace(" ","")
    char_list = [char for char in no_spaces]
    char_list= list(set(char_list))
    for each_char in char_list:
        count=user_string.count(each_char)
        print("Count for character:",each_char,"is",count)
    
  
 
user_input=input("Enter a sting")
count_char_string(user_input)
