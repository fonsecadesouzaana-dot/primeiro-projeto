import time

while True:
    opcao = int(input("""
    Menu
    1 - Somar
    2 - Subtrair
    3- Multiplicar
    4 - Dividir
    5 - Sair 
""" ))

    if opcao == 1:
        print("Somar")
    elif opcao == 2:
        print("subtrair")
    elif opcao == 3:
        print ("Multiplicar")
    elif opcao == 4:
        print ("Dividir")
    elif opcao == 5:
        print ("Sair...")
        time.sleep(1)
        break
    else:
        print ("opcao inválida, escolha uma nova.")