# berilgan sonni qo'shamiz
def add(a,b):
    result = a + b
    return result

# berilgan sonni ayiramiz
def substract(a,b):
    result = a - b
    return result

#berilgan sonni ko'paytiramiz
def multipy(a,b):
    result = a * b
    return result

def divide(a, b):
    if b == 0:
        return "Xatolik: Bo'luvchi nol bo'lishi mumkin emas!"
    else:
        result = a / b
        return result

a = int(input("a="))
print('bitta amlani tanlang "+","-","*","/"')
amal = input("amal=")
b = int(input("b="))


if amal == '+' :
    print(add(a,b))

elif amal == '-' :
    print(substract(a,b))
    
elif amal == '*' :
    print(multipy(a,b))
    
elif amal == '/' :
   print(divide(a,b))          