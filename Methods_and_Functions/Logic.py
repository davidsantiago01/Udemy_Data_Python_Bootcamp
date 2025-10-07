def even_check(num):
    if num % 2 == 0:
        return True
    else:
        return False
    
even_check(20)  
True
#-----
def check_even_list(num_list):
    for num in num_list:
        if num % 2 == 0:
            return True
    else:
        pass
check_even_list([2,5,8])
True
#-----
