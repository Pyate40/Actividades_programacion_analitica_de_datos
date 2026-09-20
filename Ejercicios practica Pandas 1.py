# %%
import pandas as pd
import numpy as np

url = "https://raw.githubusercontent.com/plotly/datasets/master/supermarket_Sales.csv"
data = pd.read_csv(url)

data = data.rename(columns={
    'Tax 5%': 'Tax',
    'Cost of goods sold': 'Cogs',
    'Gross margin percentage': 'Gross margin pct',
    'Customer stratification rating': 'Rating'
})

data.columns = (
    data.columns
        .str.strip()
        .str.lower()
        .str.replace(' ', '_')
)
# %%
# 1.Dimensiones del DataFrame
print(data.shape)
# El DataFrame contiene 1.000 registros y 17 variables, el primer número de la tupla corresponde a las filas y el segundo a las columnas.
# %%
# 2.Columnas, tipos y primeras filas
print(data.columns)
print(data.dtypes)
data.head(3)
# %%
# 3.Seleccionar varias columnas
resultado = data[['product_line','quantity','total']]
resultado.head()
# %%
# 4.¿Series o DataFrame?
print(type(data['total']))
print(type(data[['total']]))
# La segunda línea devuelve un DataFrame porque 'total' se encuentra dentro de una lista de columnas. Pandas interpreta que se solicita un subconjunto del DataFrame, aunque solamente contenga una variable.

# %%
# 5. loc y iloc sobre la misma celda
print(data.loc[7, 'product_line'])
print(data.iloc[7, 5])
# La segunda instrucción es más frágil porque iloc trabaja con la posición de la columna. Si cambia el orden de las columnas, la posición 5 puede corresponder a otra variable.

# %%
# 6. Una sola condición
mascara = data['quantity'] > 8
resultado = data[mascara]
print(resultado.shape[0])

# %%
# 7. Dos condiciones al tiempo
mascara = (data['branch'] == 'C') & (data['total'] > 300)
resultado = data[mascara]
print(resultado.shape)

# %%
# 8. Corregir un filtro por categorías
mascara = data['product_line'].isin([
    'Food and beverages',
    'Fashion accessories'
])
print(data[mascara].shape[0])

# %%
# 9. Rango de valores y columnas elegidas
mascara = (
    data['branch'].isin(['A', 'C']) &
    data['total'].between(200, 500)
)

resultado = data.loc[
    mascara,
    ['branch', 'product_line', 'quantity', 'total']
]

resultado.head()
# Resolver el filtro y la selección en una sola instrucción permite obtener directamente las filas y columnas necesarias, sin crear DataFrames intermedios.

# %%
# 10. Valor de cada unidad vendida
data['valor_unitario'] = data['total'] / data['quantity']
print(data['valor_unitario'].head(3).round(2))

# %%
# 11. Clasificar cada venta
data['tipo_compra'] = np.where(
    data['quantity'] >= 6,
    'volumen',
    'menor'
)
print(data['tipo_compra'].value_counts())
# No fue necesario recorrer las filas porque np.where evalúa toda la columna quantity y asigna el resultado de forma vectorizada.

# %%
# 12. ¿Cuánto ingreso genera cada sucursal?
resumen = (
    data
    .groupby('branch')['total']
    .sum()
)
print(resumen.round(2))

# %%
# 13. ¿Cuántas facturas registra cada método de pago?
resumen = (
    data
    .groupby('payment')['invoice_id']
    .count()
)

print(resumen)
# Cada fila representa un método de pago y muestra la cantidad de facturas registradas con ese método.

# %%
# 14. Varias métricas por método de pago
resumen = (
    data
    .groupby('payment')
    .agg(
        facturas=('invoice_id', 'size'),
        unidades=('quantity', 'sum'),
        ingreso=('total', 'sum')
    )
    .reset_index()
)

print(resumen.round(2))

# %%
# 15. Agregar la zona de cada sucursal
sucursales = pd.DataFrame({
    'branch': ['A', 'B', 'C'],
    'zona': ['Centro', 'Norte', 'Sur']
})

resultado = data.merge(
    sucursales,
    on='branch',
    how='left'
)

print(resultado.shape)
resultado[['branch', 'city', 'zona', 'total']].head()
# Para integrar dos tablas, ambas deben tener una columna en común que funcione como clave y cuyos valores permitan relacionar los registros.

# %%
# 16. La sucursal líder entre los clientes Member

# 1. Filtrar las ventas de clientes Member
ventas_member = data[data['customer_type'] == 'Member']

# 2. Agrupar por sucursal: número de facturas e ingreso total
resumen_member = (
    ventas_member
    .groupby('branch')
    .agg(
        facturas=('invoice_id', 'size'),
        ingreso=('total', 'sum')
    )
    .reset_index()
)

# 3. Calcular la columna ticket_promedio
resumen_member['ticket_promedio'] = (
    resumen_member['ingreso'] / resumen_member['facturas']
)

# 4. Ordenar de mayor a menor ingreso
resumen_member = resumen_member.sort_values(
    by='ingreso',
    ascending=False
).reset_index(drop=True)

print(resumen_member.round(2))

# 5. Escribir la conclusion
# La sucursal C lidera el ingreso total entre los clientes Member. Su ticket promedio también es el más alto, lo que indica que, en promedio, sus clientes Member gastan más por factura que los de las sucursales A y B.

# %%
