def get_grade(score):
    
    if 90 <= score <= 100 :
        return "A"
        
    elif 70 <= score <= 89:
        return "B"
        
    elif 60 <= score <= 69:
        return "C"
        
    elif 1 <= score <=59 :
        return "D"

ball = int(input("Bahoni kiriting:"))
        
result = get_grade(ball)

print(result)