import streamlit as st 
import os

st.set_page_config(page_title="Página Inicial - Curso Deploy com Streamlit",
				   page_icon = "🏠")

st.title('🏠 Página Inicial')
st.subheader('💙 Primeiro Aplicativo Web com Streamlit')

'''
---

Esse é um aplicativo Streamlit para os alunos do MBA em Data Science FLAI FAMESP.

O objetivo desse aplicativo é servir como material didático para a unidade de **Deploy com Streamlit**, da disciplina de **Programação**.

Utilizem esse material como referência para as aplicações futuras que vocês construirão. 

Sejam criativos, inovem e voem alto!


'''

c1, c2 = st.columns([4,1])

with c1:

	if os.path.exists('recursos/material.rar'):

		with open("recursos/material.rar", "rb") as file:
			material = file.read()

		st.download_button(label="📁 **Baixar material da unidade**", 
						   data = material, 
						   file_name="material-curso-deploy-com-streamlit.zip") 

with c2: 
	st.write('🚀 *#itstimetoflai*')

st.image('recursos/banner-mba.jpg')