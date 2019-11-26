def check_if_even(num):
    if num%2 == 0:
        return f"Your number {num} is even"    
    else:
       return f"Your number {num} is odd"
        
print(check_if_even(1), check_if_even(2))