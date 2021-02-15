`verificacion = False

while verificacion == False:
    name_user = input("nombre de usuario: ")
    num_letters = len(name_user)
    if num_letters in range(6,13):
        verificacion = True
    
    if verificacion == False:
        if num_letters < 6:
            print("El nombre de usuario debe contener al menos 6 caracteres")
        elif num_letters > 12:
            print("El nombre de usuario no puede contener más de 12 caracteres")
        else:
            print("El nombre de usuario no es valido")




    
print("Tu nombre de usuario " + name_user + " es valido")




