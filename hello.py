#!/usr/bin/env python3

"""Hello World Multi Linguas
Dependendo da lingua configurada no ambiente o programa exibe
a mensagem correspondente.

Como usar:

Tena a variavel Lang devidamente configurada ex:

    export LANG=pt_BR

Execucao:

    python3 hello.py
    ou
    ./hello.py
"""
__version__ = "0.0.1"
__author__ = "afcardo"
__license__ ="Unlicense"

import os

current_language = os.getenv ("LANG", "en_US")[:5]
msg = "Hello, World!"

if current_language == "pt_BR":
    msg = "Olá, Mundo!"
elif current_language == "it_IT":
    msg = "Ciao, Mondo!"
elif current_language == "es_SP":
    msg = "Hola, mundo!"

print(msg)
