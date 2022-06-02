mapa = {"km": 1000, "m": 1, "cm": 1/100, "mm": 1/1000}

try:
    valor_o = float(input("Insira o valor do comprimento: ").strip())
    uni_o = input("Insira a unidade de comprimento original: ").strip()
    v1 = mapa[uni_o]
    uni_c = input("Insira a unidade de comprimento para qual deseja converter: ").strip()
    v2 = mapa[uni_c]
except ValueError:
    print(f"Insira somente números")
except KeyError:
    print(f"Insira somente unidades de medidas válidas {tuple(mapa.keys())}.")
else:
    print(f"{str(valor_o)}{uni_o} equivale a {(v1 / v2)*valor_o}{uni_c}.")
