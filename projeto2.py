print("""
Menu Principal
  [1] Celsius para Kelvin
  [2] Celsius para Fahrenheit
  [3] Kelvin para Celsius
  [4] Kelvin para Fahrenheit
  [5] Fahrenheit para Celsius
  [6] Fahrenheit para Kelvin
  [0] SAIR
""")
opcao = int(input("Escolha uma das opções acima: "))
if opcao == 0:
    exit()
temp = float(input("Digite o valor da temperatura em graus [Celsius | Kelvin | Fahrenheit]: "))
if opcao == 1:
    print(str(temp + 273.15) + "K°")
elif opcao == 2:
    print(str(temp * 9/5 + 32) + "F°")
elif opcao == 3:
    print(str(temp - 273.15) + "C°")
elif opcao == 4:
    print(str(temp * 9/5 - 459.67) + "F°")
elif opcao == 5:
    print(str((temp - 32)*5/9) + "C°")
elif opcao == 6:
    print(str((temp + 459.67)*5/9) + "K°")
