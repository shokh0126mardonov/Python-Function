def ask_question(question: str, correct_answer: str):
    print(question)
    user_answer = input("Jvobni kiriting")
    
    if check_answer(user_answer,correct_answer):
        return "Javob to'g'ri"
    else:
        return "Javob noto'g'ri"

    
    
def check_answer(user_answer, correct_answer):   
    if user_answer.strip().lower() == correct_answer.strip().lower():
        return True
    else:
        return False
    


question = "O'zbekiston poytaxti nima? "
correct_answer = 'Toshkent'

result = ask_question(question,correct_answer)

print(result)
