import os

carpeta = "cliente_B"

if not os.path.exists("cliente_B"):
    os.mkdir("cliente_B")
    print("La carpeta 'cliente_B' fue creada.")
else:
    print("La carpeta ya existe.")
    
ruta_informes = os.path.join(carpeta, "informes")
if not os.path.exists(ruta_informes):
    os.mkdir(ruta_informes)
    print("Subcarpeta 'informes' creada.")
else:
    print("La carpeta ya existe.")


ruta_pagos = os.path.join(carpeta, "pagos")
if not os.path.exists(ruta_pagos):
    os.mkdir(ruta_pagos)
    print("Subcarpeta 'pagos' creada.")
else:
    print("La carpeta ya existe.")

    
ruta_enero = os.path.join(ruta_pagos, "enero")
if not os.path.exists(ruta_enero):
    os.mkdir(ruta_enero)
    print("Subcarpeta 'enero' creada.")
else:
    print("La carpeta ya existe.")

    
ruta_febrero = os.path.join(ruta_pagos, "febrero")
if not os.path.exists(ruta_febrero):
    os.mkdir(ruta_febrero)
    print("Subcarpeta 'febrero' fue creada.")
else:
    print("La carpeta ya existe.")

    
ruta_imagenes = os.path.join(carpeta, "imagenes")
if not os.path.exists(ruta_imagenes):
    os.mkdir(ruta_imagenes)
    print("Subcarpeta 'imagenes' fue creada.")
else:
    print("La carpeta ya existe.")