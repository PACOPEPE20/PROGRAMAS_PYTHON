input1 = float(input("Escribe el primer numero: "))
input2 = float(input("Escribe el segundo numero: "))
input3 = float(input("Escribe el tercer numero: "))


def max_de_tres(num1,num2,num3):
    if num1 > num2 and num3:
        print(num1)
    elif num2 > num3 and num1:
        print(num2)
    elif  num3 > num1 and num2:
       print(num3)      

max_de_tres(input1,input2,input3)