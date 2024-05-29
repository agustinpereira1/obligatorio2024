
def funcion():
    print("funcion que anda")

def pedirNumero():
    numero = input("Ingrese un numero ")
    try:
        int(numero)
    except ValueError:
        print("El valor ingresado no es correcto")
    else:
        print("El valor ingresado es correcto")

if __name__=="__main__":
    funcion()
    pedirNumero()

