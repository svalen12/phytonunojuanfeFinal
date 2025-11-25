#COMO USAR PANDAS PARA CREAR FILTROS

#1. importarlo
import pandas as pd

#2. traer los datos
from data.simulador import generar_ventas

#3. convertir los datos en un DATAFRAME
dataFrame=pd.DataFrame(generar_ventas())

#4. aplciar los filtros (5)
#print("dataFrame")

#yo como admin quiero ver las ventas de Eliana Restrepo
filtroUna=dataFrame.query("vendedor=='Eliana Restrepo'")
#print(filtroUna)

#yo como admin quiero ver las ventas con mas de tres productos
filtroDos=dataFrame.query("cantidad>3")
#print(filtroDos)

#yo como admin quiero ver las ventas por valores de mas de 900 mil
filtroTres=dataFrame.query("total>900000")
#print(filtroTres)

#yo como admin quiero ver las ventas de las camisetas polo
filtroCuatro=dataFrame.query("producto=='camiseta POLO'")
#print(filtroCuatro)

#yo como admin quiero ver las ventas de los productos que menos se venden
filtroCinco=dataFrame.query("producto=='Bermuda'")
print(filtroCinco)
