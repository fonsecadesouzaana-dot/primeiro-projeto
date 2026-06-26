import random
numero_gerado= random.randint (1, 20)

numero_digitado = 0
while numero_digitado != numero_gerado :
    numero_digitado= int (input("Adivinhe o numero que pensei"))
    if numero_digitado < numero_gerado:
        print("Muito baixo, tente denovo !")
    elif numero_digitado > numero_gerado:
        print("Muito alto, tente novamente!")
    else:
        print("voce acertou, Muito bem!")
        break