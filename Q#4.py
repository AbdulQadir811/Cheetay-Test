def my_function(S,F,N):
    result =0 
    for i in range(len(S)):
	    min_idx = i
	    for j in range(i+1, N):
		    if S[min_idx] > S[j]:
			    min_idx = j
	    S[i], S[min_idx] = S[min_idx], S[i]
	    F[i], F[min_idx] = F[min_idx], F[i]
    
    for i,d in enumerate(S):	
        for j in range(i,N):
            if F[i] < S[j]:
                result= result +1
                break
    return result 
