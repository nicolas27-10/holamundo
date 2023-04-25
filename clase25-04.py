n=int(input ("ingrese un numero entero: "))

while n >=1:
    for i in range (1,n):
        if n%2 ==0:
            print (f"el nunmero {i} es par")
        elif n%2 !=0:
            print (f"el nunmero {i} es impar")
    break