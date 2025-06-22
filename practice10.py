def is_strong_password(password :str):
    if len(password) > 8:
         return "strong password"
    else :
        return "wak password"
    
password = input("password kiriting = ")
    
result = is_strong_password(password)

print(result)