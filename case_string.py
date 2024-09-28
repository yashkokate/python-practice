def camel_case_string(user_input):
    words=user_input.split()
    if len(words)>0:
        words[0]=words[0].lower()
        for i in range(1,len(words)):
            words[i]=words[i].capitalize()
    final_string="".join(words)        
    return final_string

def snake_case_string(user_input):
    words = user_input.split()
    for i in range(len(words)):
        words[i] = words[i].lower()  
    final_string = "_".join(words)  
    return final_string

def kebab_case_string(user_input):
    words = user_input.split()
    for i in range(len(words)):
        words[i] = words[i].lower()  
    final_string = "-".join(words)  
    return final_string

def pascal_case_string(user_input):
    words=user_input.split()
    for i in range(0,len(words)):
        words[i]=words[i].capitalize()
    final_string="".join(words)        
    return final_string

user_string=input("Enter a string")
camel_string=camel_case_string(user_string)
pascal_string=pascal_case_string(user_string)
snake_string=snake_case_string(user_string)
kebab_string=kebab_case_string(user_string)
print(camel_string)
print(pascal_string)
print(snake_string)
print(kebab_string)