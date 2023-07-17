import streamlit as st  

st.set_page_config(page_title="Elementos de Texto do Streamlit",
				   page_icon = "📝")


st.title('📝 Elementos de Texto do Streamlit')
st.header('Subtítulo')
st.subheader('Sub-subtítulo') 

st.write('Exemplo de texto normal')
st.text('Exemplo de texto em formato de máquina (fonte courier new)')
st.caption('Exemplo de texto do tipo caption')

st.write('Identidade de Euler:')
st.latex('e^{i\pi} + 1 = 0')
st.code('''
import streamlit as st 
import numpy as np
import matplotlib.pyplot as plt

st.title('Meu Primeiro Aplicativo Web 💙')

st.header('💫 A mágica do Streamlit')

#WIDGETS
#numero
numero = st.number_input(
	label = 'Digite um número inteiro', 
	min_value = 10, 
	max_value = 1000,
	value = 100,
	step = 10
)
''')

st.info('Texto com fundo azul')
st.success('Texto com fundo verde')
st.warning('Texto com fundo amarelo')
st.error('Texto com fundo vermelho')






