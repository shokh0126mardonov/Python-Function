from random import randint

secret = randint(1,100)

print(secret) # test uchun chiqarilgan

gues = int(input("taxminiy son = "))
    

def  check_gues(secret,gues):
    if secret == gues:
        return "Correct"
    else:
        return "Incorrect"   
        
result = check_gues(secret,gues)

print(result)
