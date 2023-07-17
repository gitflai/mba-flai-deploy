import streamlit as st 
import pandas as pd
from pycaret.regression import load_model, predict_model

st.set_page_config(page_title="Modelo para Proposta de Salário",
				   page_icon = "💸",
				   layout = "wide")

modelo_carregado = load_model('recursos/modelo-previsao-de-salarios-gbr')

st.title('💸 Modelo para Proposta de Salário para Profissionais de Dados')

st.divider()

st.write("No mundo atual dos negócios, com o constante aumento da demanda por profissionais de dados, uma questão crítica que surge é: **Quanto devemos pagar aos profissionais de dados?** Neste contexto, foi desenvolvido um Modelo de Proposta de Salário para Profissionais de Dados utilizando PyCaret, uma biblioteca de aprendizado de máquina em Python que permite criar modelos preditivos de maneira rápida e eficiente, e com Streamlit para implementação e deploy.")

st.write("Esse modelo possui uma utilidade prática imensa, pois permite às empresas otimizar a alocação de recursos financeiros, ao mesmo tempo que **oferece salários justos e competitivos aos profissionais de dados**. O uso do modelo evita o sub ou super dimensionamento de salários e ajuda a atrair e reter talentos no competitivo campo da ciência de dados. Por exemplo, um varejista online pode usá-lo para determinar os salários de seus analistas de dados, enquanto uma startup de tecnologia pode usá-lo para definir a remuneração de seus engenheiros de dados. Isso oferece uma abordagem orientada a dados para um problema que tem consequências significativas tanto para as organizações quanto para os indivíduos.")

st.divider()

dados = pd.read_csv('recursos/dados tratados.csv')
 
col1, _, col2, _, col3 = st.columns([14,1,7,1,7])

with col1: 
	st.write('**Características da Vaga**')

	c1, c2 = st.columns(2)

	with c1:

		profissao = st.selectbox(label = 'Carreira', 
				options = list(dados['profissao'].unique()),
				help = 'Escolha a profissão da vaga na qual se deseja propor um salário')

		empresa = st.selectbox(label = 'Tamanho da empresa', 
				options = list(dados['empresa'].unique()),
				help = 'Escolha o tamanho da empresa da vaga na qual se deseja propor um salário')

		trabalho = st.selectbox(label = 'Modelo de contrato', 
				options = list(dados['trabalho'].unique()),
				help = 'Escolha o modelo de contrato da vaga na qual se deseja propor um salário')

		setor = st.selectbox(label = 'Setor de atuação', 
				options = list(dados['setor'].unique()),
				help = 'Escolha o setor de atuação da vaga na qual se deseja propor um salário')

	with c2: 

		modelo = st.selectbox(label = 'Tipo de vaga', 
				options = list(dados['modelo'].unique()),
				help = 'Escolha o tipo de vaga na qual se deseja propor um salário')

		nivel = st.selectbox(label = 'Nivel da vaga', 
				options = list(dados['nivel'].unique()),
				help = 'Escolha o nível da vaga na qual se deseja propor um salário')

		estado = st.selectbox(label = 'Estado da empresa', 
				options = sorted(list(dados['estado'].dropna().unique())),
				index = 20,
				help = 'Escolha a profissão da vaga na qual se deseja propor um salário')


with col2:
	st.write('**Características da Pessoa**')


	experiencia = st.selectbox(label = 'Tempo de experiência', 
			options = list(dados['experiencia'].unique()),
			help = 'Escolha o tempo de experiência do candidato que se deseja propor um salário')


	escolaridade = st.selectbox(label = 'Grau de escolaridade', 
			options = list(dados['escolaridade'].unique()),
			help = 'Escolha a escolaridade do candidato que se deseja propor um salário')

	formacao = st.selectbox(label = 'Área de formação', 
			options = list(dados['formacao'].dropna().unique()),
			help = 'Escolha a área de formação do candidato que se deseja propor um salário')


with col3:
	st.write('**Assinale as linguagens de programação que será utilizado no dia a dia de trabalho.**')

	python = st.checkbox('Linguagem Python') 

	sql = st.checkbox('Linguagem SQL') 

	r = st.checkbox('Linguagem R') 

	java = st.checkbox('Linguagem Java') 

	js = st.checkbox('Linguagem Javascript') 

	scala = st.checkbox('Linguagem Scala') 

	vba = st.checkbox('Linguagem VBA') 

st.divider()

dici = {'profissao': [profissao],
		'estado': [estado],
		'empresa': [empresa],
		'experiencia': [experiencia],
		'trabalho': [trabalho],
		'escolaridade': [escolaridade],
		'formacao': [formacao],
		'setor': [setor], 
		'modelo': [modelo],
		'nivel': [nivel],
		'linguagemPython': [1. if python else 0.],
		'linguagemSQL': [1. if sql else 0.],
		'linguagemR': [1. if r else 0.],
		'linguagemJava': [1. if java else 0.],
		'linguagemJavascript': [1. if js else 0.],
		'linguagemScala': [1. if scala else 0.],
		'linguagemVBA': [1. if vba else 0.]}


dado = pd.DataFrame(dici) 

_, col, _ = st.columns(3)

with col:
	botao = st.button(label = 'Inferir Salário',
		type = 'primary', 
		use_container_width = True)

	if botao: 
		pred = predict_model(modelo_carregado, data = dado)['prediction_label'][0]
		saida = f'## **R$ {pred:.2f}** \n é o salário estimado pelo modelo'
		st.info(saida)
