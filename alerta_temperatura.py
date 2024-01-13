#!/usr/bin/env python3

"""
Faca um script que pergunta ao usuario qual 
a temperatura

temp maior 45:alerta! Perigo calor extremo
temp x3 for maior ou igual a umidade: Alerta! perigo de calor umido
temp entre 10 e 30: normal
temp <0: Alerta frio extremo

"""
import sys
import logging
log = logging.Logger("alerta")

info = {
    "temperatura": None,
    "umidade":None
}
keys = info.keys()

for key in keys:
    try:
        info[key] = float(input(f"Qual a {key}?").strip())
    except ValueError:
        log.error(f"{key.capitalize()} inválida")
        sys.exit(1)

temp = info["temperatura"]
umidade = info["umidade"]

if temp > 45:
    print("Alerta!!! Perigo calor extremo")
elif temp * 3 >= umidade:
    print("Alerta!! Perigo de calor umido")
elif temp >= 10 and temp <= 30:
    print("Normal :D")
elif temp >= 0 and temp <=10:
    print("Frio")
elif temp < 0:
    print("Frio extremo!")








