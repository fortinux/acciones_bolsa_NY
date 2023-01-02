#!/usr/bin/env python
# coding: utf-8

# Usando Python y Yahoo! Finance para consultar acciones y títulos de la bolsa

# - biblioteca en python <https://pypi.org/project/yfinance/>
# - Inicialmente se debe instalar la biblioteca
# *yfinance* en nuestro sistema operativo:

# pip install yfinance
"""
[Obtener valores de acciones de la bolsa de NY]

Author: Fortinux - fortinux.com
Date: [2019]
Updated: [2022]
"""


# - Importamos la biblioteca en nuestro *script*
import yfinance as yf

sigla = input('Escribe la sigla de la acción: ')
sigla = yf.Ticker(sigla)

print(sigla.info)

# Muestra la información financiera
print(sigla.financials)

# Obtiene el histórico del mercado
print(sigla.history(period="max"))
