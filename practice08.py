def c_to_f(celsius):
    """_summary_
        selsiydan farangeytga o'tkazish
    Args:
        celsius (_type_): _description_
        int tipida va formulasi 
        F = (C * 9/5) + 32
    """
    F = celsius * 9/5 + 32
    
    return F

def f_to_c(fahrenheit):
    """ Farangeytdan selsiyga

    Args:
        int tipida bo'ladi
       Formula : C = (F - 32) * 5/9
    """
    C = (fahrenheit - 32) * 5/9
    
    return C

result = c_to_f(0)

print(result)
