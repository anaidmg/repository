import pandas as pd
import streamlit as st
import plotly.express as px

# Leer el archivo CSV
car_data = pd.read_csv("vehicles_us.csv")
st.title('Gráficos de visualización de datos de anuncios de coches')
st.text('Por favor selecciona el gráfico que deseas visualizar')

# Crear botones
hist_button = st.button('Histograma')
scatter_button = st.button('Gráfico de dispersión')

# Histograma
if hist_button:
    st.write(
        'Histograma para el conjunto de datos de anuncios de venta de coches')
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

# Gráfico de dispersión
if scatter_button:
    st.write('Kilometraje vs Precio)')
    fig = px.scatter(car_data, x="odometer", y="price",
                     title="Relación entre kilometraje y precio")
    st.plotly_chart(fig, use_container_width=True)
