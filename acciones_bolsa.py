#!/usr/bin/env python
# coding: utf-8

# Usando Python y Yahoo! Finance para consultar acciones y títulos de la bolsa

# - biblioteca en python <https://pypi.org/project/yfinance/>
# - Inicialmente se debe instalar la biblioteca
# *yfinance* en nuestro sistema operativo:

# pip install yfinance

# - Creamos un fichero que podemos llamar *acciones_bolsa.py*
# y lo editamos con el siguiente código:


"""
[Obtener valores de acciones de la bolsa de NY]

Author: Fortinux - fortinux.com
Date: [2019]
Updated: [2022]
"""


# - Importamos la biblioteca en nuestro *script*:

import yfinance as yf

# - Obtenemos la sigla de la acción que queremos ver y creamos
# las variables para descargar la información de Yahoo Finance:

print("***** Bolsa de valores ***** ")
print('''Para consultar el valor de las acciones de
la bolsa de Nueva York, escribe la sigla de
la acción en mayúsculas, por ej. GOOG, AAPL,
FB, AMZ, MSFT, o TSLA''')

sigla = input('Escribe la sigla de la acción: ')

sigla = yf.Ticker(sigla).info
precio_mercado = sigla['regularMarketPrice']
precio_anterior = sigla['regularMarketPreviousClose']


# - Imprimimos el valor de la acción y el del cierre anterior:

print('Precio de la acción: ', precio_mercado)
print('Precio de cierre anterior: ', precio_anterior)


# - Imprimimos la información sobre la empresa:

print(sigla['longBusinessSummary'])
