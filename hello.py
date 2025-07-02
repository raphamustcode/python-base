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
import sys

arguments = {
    "lang": None,
    "count": None,
}

for arg in sys.argv[1:]:
    # TODO: Tratar ValueError
    key, value = arg.split("=")
    key = key.lstrip("-").strip()
    value = value.strip()
    if key not in arguments:
        print(f"Invalid Option '{key}'")
        sys.exit()
    arguments[key] = value

current_language = arguments["lang"]
if current_language is None:
    current_language = os.getenv("LANG")
    # TODO: Usar repetição
    if current_language is None:
        current_language = input("Choose a language:")

current_language = current_language[:5]

msg = {
    "en_US": "Hello, World!",
    "pt_BR" : "Olá, Mundo!",
    "it_IT" : "Ciao, Mondo!",
    "es_SP" : "Hola, Mundo!",
    "fr_FR" : "Bonjour, Monde!",
}

print(
    msg[current_language] * int(arguments["count"])
)
