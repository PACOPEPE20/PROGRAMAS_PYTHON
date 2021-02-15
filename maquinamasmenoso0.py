while 1:
    print("¿NEGATIVO, POSITIVO O 0?")

    numero = float(input("Dime un numero: "))

    
    if numero < 0:
            resultado = ("Negativo")
    elif numero >0:
            resultado = ("Positivo")
    elif numero == 0:
            resultado = ("Cero")

    if numero.is_integer():
            numero = int(numero)
        
    else:
        numero = float(numero)



    print(f"El numero {numero} es {resultado}")
    

    print("--------------------------------------------------------------------------------------------")
    print("--------------------------------------------------------------------------------------------")