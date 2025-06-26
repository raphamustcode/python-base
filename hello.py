#!/usr/bin/env python3
"""Hello World Multi Linguas.

Prints the message according to the environment language.

How to use:

Has the LANG variable properly configured ex:
    export LANG=pt_BR

Execution

    python3 hello.py
    ou
    ./hello.py
"""

# Dunder (Double underline) -> __
__version__= "0.1.2"
__author__= "Rapha"
__license__= "Unlicense"

# Native Python lib. that communicates with the Operating System

import os

current_language = os.getenv("LANG", "en_us")[:5]

msg = {
    "en_US": "Hello, World!",
    "pt_BR" : "Olá, Mundo!",
    "it_IT" : "Ciao, Mondo!",
    "es_SP" : "Hola, Mundo!",
    "fr_FR" : "Bonjour, Monde!",
}

print(msg[current_language])

