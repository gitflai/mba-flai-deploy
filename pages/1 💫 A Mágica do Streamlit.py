import streamlit as st 
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="A Mágica do Streamlit",
				   page_icon = "💫")

st.title('💫 A Mágica do Streamlit')

#WIDGETS
#numero
numero = st.number_input(
	label = 'Digite um número inteiro', 
	min_value = 10, 
	max_value = 1000,
	value = 100,
	step = 10
)
#texto
texto = st.text_input('Digite o nome do gráfico:')
#cor
cor = st.color_picker('Escolha a cor desejada:')

#codigo em python 'back-end'
seq = np.random.normal(size = numero)
plt.hist(seq, color = cor, edgecolor = 'white')
plt.title(texto)

#gráfico
st.pyplot(plt)

