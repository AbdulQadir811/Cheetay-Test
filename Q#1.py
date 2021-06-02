def choose_and_swap(A):
    e_check = True
    check_2=False
    new_A = ""
    for i,d in enumerate(A):
        if A[i] == "a":
            new_A = new_A + "c"
        elif A[i] == "c":
            new_A = new_A + "a"
        else:
            new_A = new_A + A[i]
       
        if (e_check == True):
            if ord(new_A[i]) < ord(A[i]):
                e_check= False
            elif ord(new_A[i]) > ord(A[i]):
                print(f'{new_A[i]} > {A[i]}')
                check_2 = True
                e_check= False
    
    
    if check_2 == True:
        return (A)
    else:
        return (new_A)
        
    
        
#print(choose_and_swap("caac"))

