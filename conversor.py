# O processo de conversão acontece da seguinte forma:
# valor na unidade de medida inicial -> valor em metros -> valor na unidade de medida final

valor_i = float(input("Insira o valor do comprimento: "))
uni_i = input("Insira a unidade de medida inicial: ")

# Esse bloco converte o valor na unidade de medida inicial para metros
if uni_i == "m":
    em_metros = valor_i
elif uni_i == "km":
    em_metros = valor_i * 1000
elif uni_i == "cm":
    em_metros = valor_i / 100
elif uni_i == "mm":
    em_metros = valor_i / 1000
else:
    print("Unidade de medida inválida")
    exit()

uni_f = input("Insira a unidade de medida final: ")

# Esse bloco converte o valor em metros para a unidade de medida final
if uni_f == "m":
    valor_f = em_metros
elif uni_f == "km":
    valor_f = em_metros / 1000
elif uni_f == "cm":
    valor_f = em_metros * 100
elif uni_f == "mm":
    valor_f = em_metros * 1000
else:
    print("Unidade de medida inválida")
    exit()

print(f"{str(valor_i)}{uni_i} equivale a {str(valor_f)}{uni_f}")
