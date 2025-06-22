def calculate_age(birth_year,currency_year): 
    #yilni to'g'ri kirtigan hol uchun tekshirib beradi
 if currency_year >= birth_year: 
    result = currency_year - birth_year
    
    
    if result >= 18:
        return 'siz balogatga yetgansiz!'
    
    elif 0 <= result < 18:
        return f"siz hali balog'atga yetishingizga {18-result} yil bor"
    
  
 else:  #xato kiritilgan yil uchun else ishlaydi 
      print('siz noto\'g\'ri yil kiritgansiz')
 
 
birth_year = int(input("tug'ilgan yilingizni kiriting = ")) 
currency_year = int(input("hozirgi yilni  kiriting = ")) 
 
result1 = calculate_age(birth_year,currency_year)

print(result1)
 