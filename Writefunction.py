def is_leap(year):
    if year % 4 != 0:
        return False
    
    if year % 100 == 0 and year % 400 != 0:
        return False
    
    return True
    
        
    # Write your logic here
