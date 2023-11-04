# Crear un nuevo libro de Excel
import openpyxl
workbook = openpyxl.Workbook()

# Seleccionar la hoja activa
sheet = workbook.active
sheet.title = "Lista de Supermercados"

# Agregar encabezados en hoja de datos
sheet["A1"] = "Supermercado"
sheet["B1"] = "Producto"
sheet["C1"] = "Precio"



# Lista de supermercados con nombre de producto y precio
supermarkets = [
    ("Supermercado A", "Manzanas", 2.99),
    ("Supermercado A", "Peras", 3.49),
    ("Supermercado B", "Naranjas", 2.79),
    ("Supermercado B", "Kiwi", 3.29),
    # Agrega más productos y precios aquí
]




# Agregar datos a la hoja
for data in supermarkets:
    sheet.append(data)
    

# Guardar el archivo Excel
workbook.save("lista_supermercados.xlsx")

# Cerrar el archivo Excel
workbook.close()
