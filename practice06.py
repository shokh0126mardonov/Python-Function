def is_valid_phone_number(phone):
    
    if len(phone) == 9 and phone.isdigit() :
        return 'True'
    else:
        return "False"
        
phone = input("phone_number = ").replace(" ",'')
        
result = is_valid_phone_number(phone)   

print(result)
    