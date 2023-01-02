#!/home/usuario/gitRepos/ejemplos/bin/python python
"""
[Obtener valores de acciones de la bolsa de NY]

Author: Fortinux - fortinux.com
Date: [2019]
Updated: [2022]
"""
# Crea un gráfico con los valores de la acción
# Se importan las bibliotecas necesarias
import yfinance as yf
import matplotlib.pyplot as plt


# Se pueden modificar las fechas de las variables start y end a discreción
start = '2020-01-01'
end = '2022-05-01'

sigla = input('Escribe la sigla de la acción: ')
sigla = yf.download(sigla, start, end)

sigla['Open'].plot(label='Acción', figsize=(15, 7))
plt.title('Valor de la acción período enero 2020 a abril 2022')
