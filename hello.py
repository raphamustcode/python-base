#!/usr/bin/env python3
"""Hello World Multi Linguas.

Dependendo da língua configurada no ambiente o programa exibe a mensagem 
correspondente.

Como usar:

Tenha a variável LANG devidamente configurada ex:

    export LANG=pt_BR

Execução

    python3 hello.py
    ou
    ./hello.py
"""

# Dunder (Double underline) -> __
__version__= "0.0.1"
__author__= "Rapha"
__license__= "Unlicense"

# Native Python lib. to communicate with the Operating System

import os

# CurrentLanguage -> Pascal Case
# current_language -> Snake Case
current_language = os.getenv("LANG", "en_us")[:5]

# Variable
msg = "Hello World!"

# Condition (statment) blocks
if current_language == "pt_BR":
    msg = "Olá Mundo!"
elif current_language == "it_IT":
    msg = "Ciao Mondo!"
elif current_language == "es_SP":
    msg = "Hola Mundo!"
elif current_language == "fr_FR":
    msg = "Bonjour Monde!"

print(msg)

