import math

#Funcion de Calculos
def volumen_cilindro(radiocilindro :float, alturacilindro :float) ->float:
    # Formula
    # v = pir(caret2)h
    volumen = math.pi * (radiocilindro ** 2) * alturacilindro
    return volumen

#Calculo de area de cilindro
def area_cilindro(radiocilindro :float, alturacilindro :float) -> float:
    area_lateral = 2 * math.pi * radiocilindro * alturacilindro
    area_base = 2 * math.pi * (radiocilindro ** 2)
    # resultado_area = (2*math.pi)*(radiocilindro)*(alturacilindro) + (2*math.pi) *(math.pow(radiocilindro,2))
    return area_lateral + area_base

#Salida general del usuario
def main():
    radio = float(input("Introduce el radio del cilindro: "))
    altura = float(input("Introduce la altura del cilindro: "))

    # Recibir resultados
    volumen = volumen_cilindro(radio, altura)
    resultado_area = area_cilindro(radio, altura)
    print(f"El area final es de {resultado_area:.2f} m^2")
    print(f"El volumen final es de {volumen:.2f} m^3")

main()
