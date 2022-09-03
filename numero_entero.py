# programa No 2 mostrar el numero mayor

print("------------------------------------------------")
print("---escriba tres numeros para mostrar el valor---")
print("------------------------------------------------")
#input
a= input("digite el primer numero")
a= (a)

b = input("diite el segundo valor")
b= (b)

C = input("digite el tercer valor")
c= (C)

#processing
if a>b:
    if a>C:
        mayor=a
    else:
        mayor=C
else:
        if b>C:
             mayor = C
        else:
                mayor = C
        
# output

print("----------------")
print("---resultados---")
print("----------------")
print("el numero mayor:"+str(mayor))
