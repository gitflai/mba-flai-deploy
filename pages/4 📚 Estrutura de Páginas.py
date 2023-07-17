import streamlit as st 
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="Estrutura de Páginas",
				   page_icon = "📚")

st.title('📚 Estrutura de Páginas')
'''
Pode ser feita de duas maneiras:

- Utilizando estruturas de IFs, como exemplificado nessa sub-página.
- Utilizando a pasta 'pages', permitindo um arquivo '.py' único para cadá sub-página.

'''

paginas = ['Página 1',
		   'Página 2',
		   'Página 3']

pagina = st.radio('Escolha uma página', paginas)
 
	



if pagina == 'Página 1':
	st.title('Página 1') 
	st.write('Conteúdo da Página 1')


if pagina == 'Página 2':
	st.title('Página 2') 
	st.write('Conteúdo da Página 2')


if pagina == 'Página 3':
	st.title('Página 3') 
	st.write('Conteúdo da Página 3')
 





