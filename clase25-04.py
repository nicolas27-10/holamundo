n=int(input ("ingrese un numero entero: "))

while n >=1:
    for i in range (1,n):
        if i%2 ==0:
            print (f"el nunmero {i} es par")
        elif i%2 !=0:
            print (f"el nunmero {i} es impar")
    break