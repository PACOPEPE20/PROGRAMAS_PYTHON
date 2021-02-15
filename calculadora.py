
titulo_calculadora = True

while 1:
        
        if titulo_calculadora == True:

                print("XXXXXXXXXXXXXXXXXXXXXXX")
                print("      CALCULADORA")
                print("XXXXXXXXXXXXXXXXXXXXXXX")
        try:
                num_1 = float(input("Dime el primer numero: "))
                op = input("Dime el operador: ")
                num_2 =  float(input("Dime el segundo numero: "))
      

                
                if op == "+":
                        resultado = num_1 + num_2
                elif op =="-":
                        resultado = num_1 - num_2
                elif op == "*":
                        resultado = num_1 * num_2
                elif op == "/":
                        resultado = num_1 / num_2
                elif op == "^":
                        resultado = num_1 ** num_2
                else:
                        print("EL OPERADOR NO ES VALIDO")

                if resultado.is_integer():
                        resultado = int(resultado)
                        num_1 = int(num_1)
                        num_2 = int(num_2)
                        print("El resultado " + (str(num_1)) + " " + (str(op)) + " " + (str(num_2)) + " es igual a " + (str(resultado)))
                
                else:
                        
                        resultado = round(resultado,1)
                        num_1 = float((num_1))
                        num_2 = float((num_2))
                        print("El resultado " + (str(num_1)) + " " + (str(op)) + " " + (str(num_2)) + " es igual a " + (str(resultado)))
                        
                
                
                print("-----------------------")
                print("   HAZ OTRO CÁLCULO")
                print("-----------------------")
                titulo_calculadora = False
                
        

                

          
        except ValueError:
                print("NO HAS PUESTO UN NUMERO")
                print("-----------------------")
                print(" VUELVE HA INTENTARLO")
                print("-----------------------")
                titulo_calculadora = False

                

