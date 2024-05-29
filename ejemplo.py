
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

def factorial(valor):
    factorial = 1
    if valor < 0:
        print("El valor ingresaro no es correcto")
    else:
        while valor != 0:
            factorial = factorial * valor
            valor-=1
    print("El factorial de ", valor, "es", factorial)


if __name__=="__main__":
    funcion()
    pedirNumero()
    numero = int(input("Ingrese un numero "))
    factorial(numero)

