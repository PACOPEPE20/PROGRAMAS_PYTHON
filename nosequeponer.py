#preguntar cantidad a invertir, el interés porcentual anual y el número de años,
#y mostrar el capital obtenido en la inversión redondeado con dos decimales.

invertido = float(input("Caunto has invertido: "))
interes = float(input("Cuanto porciento de interes te has llevado por año: "))
Años = int(input("Cuantos años: "))
interes_en_porcentaje = str(interes) + "%"
interes2 = interes / 100
if Años ==1:
    año_sinorplu = "año"
else:
    año_sinorplu = "años" 

capital_obtenido = invertido * interes2 * Años
capital_final = capital_obtenido + invertido
capital_final_rodeado = round(capital_final,2)

print(f"Invirtiendo {invertido} euros, con un  interes de {interes2} al año, en {Años} {año_sinorplu} ..." )
print(f"Has obtenido un capital de {capital_final} ")