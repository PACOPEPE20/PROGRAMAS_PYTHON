


name_user = input("nombre de usuario: ")
num_letters = len(name_user.strip())
print(num_letters)


if num_letters in  range(6,13):
    print("Correcto")
else:
    print("Invalido")
    