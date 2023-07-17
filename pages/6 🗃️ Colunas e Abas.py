import streamlit as st 

st.set_page_config(page_title="Colunas e Abas",
				   page_icon = "🗃️")

st.title('🗃️ Colunas e Abas')

# metodo direto
col1, col2 = st.columns(2)
col1.header('Primeira Coluna') 
col2.header('Segunda Coluna')

col1.write('Esse é o conteúdo da primeira coluna. Esse é o conteúdo da primeira coluna')
col2.write('Esse é o conteúdo da segunda coluna. Esse é o conteúdo da segunda coluna')


st.divider()

# metodo mais organizado

col1, col2 = st.columns(2)

with col1:
	st.header('Primeira Coluna') 
	st.write('Esse é o conteúdo da primeira coluna. Esse é o conteúdo da primeira coluna')

with col2:
	st.header('Segunda Coluna') 
	st.write('Esse é o conteúdo da segunda coluna. Esse é o conteúdo da segunda coluna')


st.divider()

# proporcoes
col1, col2, col3 = st.columns([1,2,1])

with col1:
	st.header('Primeira Coluna') 
	st.write('Esse é o conteúdo da primeira coluna. Esse é o conteúdo da primeira coluna')

with col2:
	st.header('Segunda Coluna') 
	st.write('Esse é o conteúdo da segunda coluna. Esse é o conteúdo da segunda coluna')

with col3:
	st.header('Terceira Coluna') 
	st.write('Esse é o conteúdo da terceira coluna. Esse é o conteúdo da terceira coluna')


st.divider()

# espaço entre colunas
col1, _, col2, _, col3 = st.columns([10,1,4,1,4])

with col1:
	st.header('Primeira Coluna') 
	st.write('Esse é o conteúdo da primeira coluna. Esse é o conteúdo da primeira coluna')

with col2:
	st.header('Segunda Coluna') 
	st.write('Esse é o conteúdo da segunda coluna. Esse é o conteúdo da segunda coluna')

with col3:
	st.header('Terceira Coluna') 
	st.write('Esse é o conteúdo da terceira coluna. Esse é o conteúdo da terceira coluna')


st.divider()


# abas

abas = ['Primeira Aba', 'Segunda Aba', 'Terceira Aba']
aba1, aba2, aba3 = st.tabs(abas)


with aba1:
	st.header('Primeira Aba') 
	st.write('Esse é o conteúdo da primeira aba. Esse é o conteúdo da primeira aba')

with aba2:
	st.header('Segunda Aba') 
	st.write('Esse é o conteúdo da segunda aba. Esse é o conteúdo da segunda aba')

with aba3:
	st.header('Terceira Aba') 
	st.write('Esse é o conteúdo da terceira aba. Esse é o conteúdo da terceira aba')

	col1, col2 = st.columns([1,2])

	with col1:
		st.header('Primeira Coluna') 
		st.write('Esse é o conteúdo da primeira coluna. Esse é o conteúdo da primeira coluna')

	with col2:
		st.header('Segunda Coluna') 
		st.write('Esse é o conteúdo da segunda coluna. Esse é o conteúdo da segunda coluna')



