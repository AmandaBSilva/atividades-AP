# dicionário das unidades de medida em relação a metros
dicionario = {"km": 1000, "m": 1, "cm": 1/100, "mm": 1/1000}

valor_o = float(input("Insira o valor do comprimento: "))

uni_o = input("Insira a unidade de comprimento original: ")
if uni_o not in dicionario.keys():
    print(f"Unidade de comprimento inválida. As unidade válidas são {list(dicionario.keys())}")
    exit()  # Para o programa se uni_o não aparece no dicionário

uni_c = input("Insira a unidade de comprimento para qual deseja converter: ")
if uni_c not in dicionario.keys():
    print(f"Unidade de comprimento inválida. As unidade válidas são {list(dicionario.keys())}")
    exit()  # Para o programa se uni_c não aparece no dicionário

valor_c = valor_o * dicionario[uni_o] / dicionario[uni_c]
print(f"{str(valor_o)}{uni_o} equivale a {str(valor_c)}{uni_c}.")
