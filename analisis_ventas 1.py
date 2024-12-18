import pandas as pd
import matplotlib.pyplot as plt

# Cargar los datos del CSV
data = pd.read_csv("ventas_productos.csv")

# Calcular el precio total por producto
data['Precio_Total'] = data['Cantidad'] * data['Precio']

# Mostrar los resultados
print("Datos con Precio Total:")
print(data)

# Crear un gráfico de barras
plt.bar(data['Productos'], data['Precio_Total'], color='skyblue')
plt.title("Precio Total por Producto")
plt.xlabel("Productos")
plt.ylabel("Precio Total")
plt.xticks(rotation=45)

# Guardar el gráfico como imagen PNG
plt.tight_layout()
plt.savefig("precio_total_productos.png")
plt.show()
