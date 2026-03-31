def rec_min(L):
    if len(L)==1:
        return L[0]
    else:
        m=rec_min(L[1:])
        return L[0] if L[0]<m else m
print(rec_min([5,45,2,1,5]))