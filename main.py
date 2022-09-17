import numpy as np 

a = float(input("Enter 'a' : "))
b = float(input("Enter 'b' : "))
c = float(input("Enter 'c' : "))
d = float(input("Enter 'd' : "))
e = float(input("Enter 'e' : "))
f = float(input("Enter 'f' : "))
g = float(input("Enter 'g' : "))
h = float(input("Enter 'h' : "))
i = float(input("Enter 'i' : "))
j = float(input("Enter 'j' : "))
k = float(input("Enter 'k' : "))
l = float(input("Enter 'l' : "))
def Cramers_Rule_3_Equations():
    det = int(np.linalg.det(np.array([[a,b,c],
                                  [d,e,f], 
                                  [g,h,i]])))
    if det==0:
        print("det cannot equal to 0")
    det_x = int(np.linalg.det(np.array([[j,b,c],
                                    [k,e,f], 
                                    [l,h,i]])))

    det_y = int(np.linalg.det(np.array([[a,j,c],
                                    [d,k,f], 
                                    [g,l,i]])))

    det_z = int(np.linalg.det(np.array([[a,b,j],
                                    [d,e,k], 
                                    [g,h,l]])))
    x= det_x/det
    y=det_y/det
    z=det_z/det
    return x,y,z
print("x, y and z :",Cramers_Rule_3_Equations())