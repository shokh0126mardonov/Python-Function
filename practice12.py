def calculate_bmi(weight : float ,height:float):
    '''bu yerda vaznni hisoblab olamiz keyingi funksiyada
    esa qanaqa darajada kirishini topib olamiz'''
    
    bmi = weight/(height**2)
    return round(bmi,2)

def  bmi_status(bmi:float):
    
    if 0 <= bmi <= 18.4:
        return "Juda ozg'in"
    
    elif 18.5 <= bmi <= 24.9 :
        return "Normal" 
    
    elif 25 <= bmi <= 29.9:
        return "ortib ketgan vazn"
    
    elif 30 <= bmi:
        return "semizlik"
    
    
weight = float(input("vazn = "))        
height = float(input("bo'yi = ")) 

bmi = calculate_bmi(weight,height)

result = bmi_status(bmi)       

print(result)
    
    
    