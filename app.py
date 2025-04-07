import streamlit as st
import pandas as pd

if "mostrar" not in st.session_state:
    st.session_state.mostrar = False

st.title("Mi primera app en Streamlit")
st.write("**¡Hola Mundo!**")

url_data = "https://raw.githubusercontent.com/mwaskom/seaborn-data/refs/heads/master/tips.csv"
df = pd.read_csv(url_data)

st.header("Dataset de tips")
min_tip = st.slider("Seleccione un valor mínimo",
                    min_value=1.0, max_value=10.0, step=0.5)
st.dataframe(df.query("tip>=@min_tip"))

st.subheader("Propina promedio por día de la semana")
tip_by = df.groupby("day")["tip"].mean()
st.bar_chart(tip_by)

if not st.session_state.mostrar:
    if st.button("Mostrar histograma"):
        st.session_state.mostrar = True
        st.rerun()
else:
    st.write("El usuario ya presionó el botón")
    st.subheader("Histograma de la cuenta")
    ax = df["tip"].hist()
    st.pyplot(ax.figure)
    st.rerun()
