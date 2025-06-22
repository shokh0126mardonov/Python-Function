def deposit(balance, amount) :
    """Balansga pul qo'shish

    Args:
        balance (_type_): int tipida bo'ladi
        amount (_type_): int tipida bo'ladi
    """
    balance += amount
    return f"sizning hisobingizga {balance} pul bor"

def withdraw(balance, amount):
    """Balansdan pul ayirish

    Args:
        sonlar int tipida kiritiladi balans 
        amountdan katta bo'lishi kerak

    Returns:
        _type_: _description_
    """
    if balance >= amount:
        balance -= amount
        return f"sizning hisobingizga {balance} pul bor"
    else:
        return "Balansizngizda pul yetarli emas"
  

balance = int(input("balanc = "))
amount = int(input("amount = "))

# result = deposit(balance,amount)

result = int(input("---Amalni tanlang---""\n"
               "1.Balansga pul qo'shish""\n"
               "2.Balansdan pul ayirish "))

if result == 1:
    natija = deposit(balance,amount)
elif result == 2:
    natija = withdraw(balance,amount)

print(natija)