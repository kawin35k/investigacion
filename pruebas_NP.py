import numpy as np
a=2
lista=[1,5,4,3,2,7,8,9,9,5]
arr=np.array(lista)
brr=np.empty(a,dtype=int)
b=np.concatenate((arr,[100]),axis=0)
print(b)
