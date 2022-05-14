#!/usr/bin/env python
# coding: utf-8

# Usando Python y Yahoo! Finance para consultar acciones y títulos de la bolsa   

# - biblioteca en python <https://pypi.org/project/yfinance/> 
# - Inicialmente se debe instalar la biblioteca *yfinance* en nuestro sistema operativo:

# pip install yfinance

# - Creamos un fichero que podemos llamar *acciones_bolsa.py* y lo editamos con el siguiente código:

#!/user/bin/env python3
"""
[Obtener valores de acciones de la bolsa de NY]

Author: Fortinux - fortinux.com
Date: [2019]
"""


# - Importamos la biblioteca en nuestro *script*:

import yfinance as yf

# - Obtenemos la sigla de la acción que queremos ver y creamos las variables para descargar la información de Yahoo Finance:

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


# - Aquí os dejo otros tres ejemplos para adaptar nuestro script: 
# Descomentar para poder ejecutar el código
# sigla = input('Escribe la sigla de la acción: ')

# sigla = yf.Ticker(sigla)
# sigla.info

# # Muestra la información financiera
# sigla.financials

# # Obtiene el histórico del mercado
# sigla.history(period="max")


# # Crea un gráfico con los valores de la acción: 
# # Se importan las bibliotecas necesarias
# import datetime
# import matplotlib.pyplot as plt


# start = '2020-01-01'
# end = '2022-05-01'
# sigla = input('Escribe la sigla de la acción: ')
# sigla = yf.download(sigla, start, end)

# sigla['Open'].plot(label = 'Acción', figsize = (15,7)) 
# plt.title('Valor de la acción período enero 2020 a abril 2022')
