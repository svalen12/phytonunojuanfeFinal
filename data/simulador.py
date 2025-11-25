#contruir un codigo de py que genere mil datos asociado a las ventas de un local de ropa 

#MOCK ejercicio que utilizamos para sumilar datos 
#def funcion en py
import random
from datetime import datetime,timedelta

def generar_ventas():

    productos=[
        {"nombre": "camiseta POLO","precio":150000},
        {"nombre": "pantalon clasico","precio":300000},
        {"nombre": "chaqueta chevignon","precio":450000},
        {"nombre": "camisa leñadora","precio":200000},
        {"nombre": "Bermuda","precio":130000}
        #10 productos mas
    ]

    tallas=["S","M","L","XL"]
    vendedores=["Juan Morales","Emma Aristizabal","Eliana Restrepo","Juan Muñoz","Juan gil",]

    tiendas=["santafe","portal 80","puerta del norte","viva envigado","oviedo"]

    fechaInicio=datetime(2025,1,1)

    #Generando 1000 ventas
    ventas=[]
    for _ in range(1000):
        producto=random.choice(productos)
        cantidad=random.randint(1,8)
        fecha=fechaInicio+timedelta(days=random.randint(0,90))
        ventas.append(
            {
                "producto":producto["nombre"],
                "precioUnitario":producto["precio"],
                "talla":random.choice(tallas),
                "tienda":random.choice(tiendas),
                "cantidad":cantidad,
                "vendedor":random.choice(vendedores),
                "total":cantidad*producto["precio"]

            }
        )
    return(ventas)


