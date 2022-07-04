opcao = input("Escolha uma das opções acima: ")
if opcao == 0:
    return
temp = float(input("Digite o valor da temperatura em graus [Celsius | Kelvin | Fahrenheit]: "))
if opcao == 1:
    print(str(temp + 273.15) + "K°")
elif opcao == 2:
    print(str(temp * 9/5 + 32) + "F°")
elif opcao == 3:
    print(str(temp - 273.15) + "C°")
elif opcao == 4:
    print(str(temp * 9/5 - 459.67) + "K°")
elif opcao == 5:
    print(str((temp - 32)*5/9) + "C°")
elif opcao == 6:
    print(str((temp + 459.67)*5/9) + "F°")
