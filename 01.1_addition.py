def add_integers(a,b):
    return a + b

def add_floats(a, b):
    return a + b    

def add_complex(a, b):
    return a + b


num1=10
num2=12.5
num3=30+5j
num4=20+10j
result_int = add_integers(num1, num2)
result_float = add_floats(num1, num2)
result_complex = add_complex(num3, num4)
print("the sum of integers is ", result_int)
print("the sum of floats is ", result_float)                                                                        
print("the sum of complex numbers is ", result_complex)