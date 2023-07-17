import streamlit as st 
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Dashboard - O Perfil do Profissional de Dados no Brasil",
				   page_icon = "📊",
				   layout = "wide")

st.title('📊 O Perfil do Profissional de Dados no Brasil')

st.divider()

st.write('O State of Data Brazil 2021, uma ampla pesquisa sobre o mercado de trabalho em dados no Brasil, foi conduzida por Data Hackers e Bain & Company. Realizada online de outubro a dezembro de 2021, a pesquisa coletou dados de 2.645 participantes de todo o país, abordando variados aspectos como demografia, formação, papel e experiência no setor, remuneração, turnover e satisfação no trabalho, incluindo o impacto do teletrabalho. Para preservar a privacidade, os dados foram anonimizados, com a remoção de outliers e informações potencialmente identificáveis, resultando na ausência de alguns dados coletados na versão final do dataset.')

st.write('Veja agora o desenvolvimento de dashboards interativos com o objetivo de proporcionar uma análise rica e intuitiva dos dados. Essas ferramentas nos permitem traçar um perfil abrangente do profissional de dados no Brasil. Não se trata apenas de apresentar números e gráficos, mas de permitir que os usuários explorem os dados, compreendam tendências e extraiam insights valiosos. Isso tudo contribui para uma compreensão mais profunda e uma visualização mais clara do panorama atual do mercado de trabalho na área de dados no país.')

dados = pd.read_csv('recursos/dados tratados.csv')
 

st.divider()



st.subheader('🔹 Insira as informações das quais deseja filtrar a base de dados') 


col1, _, col2, _, col3, _, col4 = st.columns([2, .2, 2, .2, 2, .2, 4])


with col1: 
	ida = st.checkbox('Filtrar por idade?')
	idademin, idademax = st.slider(label = 'Selecione a idade:',
		min_value = int(dados['idade'].min()),
		max_value = int(dados['idade'].max()),
		value = [int(dados['idade'].min()), int(dados['idade'].max())],
		step = 1,
		help = 'Selecione as idades para filtrar os dados da dashboard',
		disabled = not ida)

with col2:
	sex = st.checkbox('Filtrar por gênero?')
	sexo = st.selectbox(label = 'Gênero', 
		options = list(dados['sexo'].unique()),
		index = 0,  
		help = 'Escolha um gênero para filtrar a dashboard',
		disabled = not sex)


with col3:
	car = st.checkbox('Filtrar por carreira?')
	carreira = st.radio(label = 'Carreira', 
		options = list(dados.profissao.unique()),
		index = 1,  
		help = 'Escolha uma carreira para filtrar a dashboard',
		disabled = not car)


with col4:
	reg = st.checkbox('Filtrar por região?')
	regioes = dados.regiao.unique()
	regiao = st.multiselect(label = 'Região', 
		options = regioes, 
		default = regioes,  
		help = 'Escolha uma ou mais regiões para filtrar a dashboard',
		disabled = not reg)


def filtra_dados(dados):
    if ida:
        dados = dados[(dados['idade'] >= idademin) & (dados['idade'] <= idademax)]
    if sex:
        dados = dados[dados['sexo'] == sexo]
    if reg:
        dados = dados[dados['regiao'].isin(regiao)]
    if car:
        dados = dados[dados['profissao'] == carreira]
    return dados

# dados filtrados
dados = filtra_dados(dados)


# funçoes utilizadas
def grafico_perfil(var, titulo, max = None):
    aux = pd.DataFrame()
    aux['Contagem'] = dados[var].value_counts()
    aux['Frequencia'] = dados[var].value_counts(normalize = True)
    if max is not None:
        aux = aux.iloc[:max, :]
    fig = px.bar(x = '<b>' + aux.index + '</b>',
                y = aux.Contagem,
                labels = {'x': '', 'y': ''},
                title = '<b>' + titulo + '</b>')
    fig.update_traces(texttemplate = [f'{v:.1%} 'for v in aux.Frequencia],
                    textposition = 'auto')
    st.plotly_chart(fig, use_container_width = True)


def grafico_linguagens(titulo):
    aux = pd.DataFrame()
    aux['Frequencia'] = dados.filter(regex = 'linguagem').mean()
    aux['Contagem'] = dados.filter(regex = 'linguagem').sum().astype(int)
    aux.index = [aux.index[i].replace('linguagem', '') for i in range(7)]
    aux.sort_values(by = 'Contagem', ascending = False, inplace = True)
    fig = px.bar(x = '<b>' + aux.index + '</b>',
                y = aux.Contagem,
                labels = {'x': '', 'y': ''},
                title = '<b>' + titulo + '</b>')
    fig.update_traces(texttemplate = [f'{v:.1%} 'for v in aux.Frequencia],
                    textposition = 'auto')
    st.plotly_chart(fig, use_container_width = True)


def grafico_idades(titulo):
    fig = px.histogram(dados.idade, title = '<b>' + titulo + '</b>')
    fig.update_traces(marker = dict(line=dict(color='white', width=2)))
    fig.update_layout(showlegend=False)
    fig.update_xaxes(title_text="")
    fig.update_yaxes(title_text="")
    st.plotly_chart(fig, use_container_width = True)


def grafico_salario(titulo):
    aux = pd.DataFrame()
    aux['Contagem'] = dados['salario'].value_counts().sort_index()
    aux['Frequencia'] = dados['salario'].value_counts(normalize = True)
    fig = px.bar(x = '<b>' + (aux.index/1000).astype(str) + 'k' + '</b>',
                y = aux.Contagem,
                labels = {'x': '', 'y': ''},
                title = '<b>' + titulo + '</b>')
    fig.update_traces(texttemplate = [f'{v:.1%} 'for v in aux.Frequencia],
                    textposition = 'auto')
    st.plotly_chart(fig, use_container_width = True)


def grafico_salario_por_variavel(var, titulo, max = None, altura = 400):
    aux = pd.DataFrame()
    aux['Salario'] = dados.groupby(var).mean(numeric_only = True)['salario'].round(2)
    aux['Contagem'] = dados.groupby(var).count()['salario']
    aux.sort_values(by = 'Salario', ascending = False, inplace = True)
    if max is not None:
        aux = aux.iloc[:max, :]
    aux = aux.iloc[::-1]
    titulo0 = '🔹 Salário por ' + titulo.upper()
    fig = px.bar(y = '<b>' + aux.index + '</b>',
                 x = aux.Salario,
                 labels = {'x': '', 'y': ''},
                 title = '<b>' + titulo0 + '</b>')
    fig.update_traces(texttemplate = [f'<b>R$ {v:.2f}</b> <br> ({c})' for v, c in zip(aux.Salario, aux.Contagem)],
                      textposition = 'auto')
    fig.update_layout(height = altura)
    st.plotly_chart(fig, use_container_width = True)
 

st.divider()

abas = ['🔹 O Perfil do Profissional de Dados no Brasil', 
		'🔹 Painel de Remuneração: Revelando o Cenário Salarial',
		'🔹 Explorar e Baixar os Dados Filtrados',
		'🔹 Exercícios!!!']

aba1, aba2, aba3, aba4 = st.tabs(abas)

with aba1:
	st.header(abas[0])
	st.write('A dashboard apresenta informações relevantes e insights sobre o perfil dos profissionais de dados no cenário brasileiro. Essa ferramenta fornece uma análise abrangente, permitindo compreender as características, competências, experiências e tendências desse segmento em constante crescimento.')

	st.divider()

	cols = st.columns([1.5, 2.5, 3, 3, 3, 3, 3, 2])

	with cols[0]:
		st.metric('🔹Amostras', dados.shape[0])

	with cols[1]:
		st.metric('🔹Idade', f'{dados.idade.mean():.0f} anos')

	with cols[2]:
		st.metric('🔹Escolaridade', dados.escolaridade.value_counts().index[0])

	with cols[3]:
		st.metric('🔹Setor', dados.setor.value_counts().index[0])

	with cols[4]:
		st.metric('🔹Formação', dados.formacao.value_counts().index[0])

	with cols[5]:
		st.metric('🔹Experiência', dados.experiencia.value_counts().index[0])

	with cols[6]:
		st.metric('🔹Salário', f'R$ {dados.salario.mean():.2f}')

	with cols[7]:
		st.metric('🔹Satisfação', f'{100*dados.satisfacao.mean():.1f}%')
 

	col1, col2, col3 = st.columns([7,6,4])

	with col1:
		grafico_perfil('experiencia', '🔹 TEMPO DE EXPERIÊNCIA', max = 7)

	with col2:
		grafico_perfil('escolaridade', '🔹 GRAU DE ESCOLARIDADE', max = 7)

	with col3:
		grafico_perfil('estado', '🔹 ESTADO', max = 5)




	col1, col2, col3, col4, col5 = st.columns([4,3,3,3,3])

	with col1:
 		grafico_perfil('trabalho', titulo = '🔹 TIPO DE CONTRATO', max = 5)

	with col2:
 		grafico_perfil('empresa', titulo = '🔹 TAMANHO DA EMPRESA', max = 3)

	with col3:
 		grafico_perfil('modelo', titulo = '🔹 MODELO DE TRABALHO', max = 3) 

	with col4:
 		grafico_perfil('nivel', titulo = '🔹 CARGO', max = 5)

	with col5:
 		grafico_perfil('sexo', titulo = '🔹 GÊNERO', max = 3)



	col1, col2 = st.columns(2)

	with col1:
 		grafico_perfil('formacao', titulo = '🔹 ÁREA DE FORMAÇÃO' )

	with col2:
 		grafico_perfil('setor', titulo = '🔹 SETOR DE ATUAÇÃO', max = 8)
 



	col1, col2, col3 = st.columns([3,4,3])

	with col1:
 		grafico_idades(titulo = '🔹 DISTRIBUIÇÃO DAS IDADES')

	with col2:
 		grafico_salario(titulo = '🔹 DISTRIBUIÇÃO DOS SALÁRIOS')

	with col3:
 		grafico_linguagens(titulo = '🔹 LINGUAGENS MAIS UTILIZADAS')

 

with aba2:
	st.header(abas[1])	
	st.write('Essa dashboard oferece informações valiosas sobre salários em diversos setores e cargos profissionais. Essa dashboard permite explorar e analisar dados salariais de forma interativa, fornecendo insights relevantes para profissionais, empresas e pesquisadores interessados em compreender melhor o panorama salarial em diferentes áreas de atuação.')

	st.divider()

	col1, col2, col3 = st.columns(3)

	with col1:
		grafico_salario_por_variavel('experiencia', titulo = 'Tempo de Experiência', max = 7, altura = 550) 
	with col2:
		grafico_salario_por_variavel('escolaridade', titulo = 'Grau de Escolaridade', max = 7, altura = 550) 
	with col3:
		grafico_salario_por_variavel('trabalho', titulo = 'Tipo de Contrato', max = 7, altura = 550) 


	col1, col2, col3, col4 = st.columns(4)

	with col1:
		grafico_salario_por_variavel('nivel', titulo = 'Tipo de Cargo', max = 3, altura = 350)
	with col2:
		grafico_salario_por_variavel('empresa', titulo = 'Tamanho de Empresa', max = 3, altura = 350)
	with col3:
		grafico_salario_por_variavel('modelo', titulo = 'Modelo de Trabalho', max = 3, altura = 350)
	with col4:
		grafico_salario_por_variavel('sexo', titulo = 'Gênero', max = 3, altura = 350)


	col1, col2, col3 = st.columns(3)

	with col1:
		grafico_salario_por_variavel('setor', titulo = 'Setor de Atuação', max = 10, altura = 700) 
	with col2:
		grafico_salario_por_variavel('formacao', titulo = 'Área de Formação', max = 10, altura = 700)
	with col3:
		grafico_salario_por_variavel('estado', titulo = 'Estado', max = 10, altura = 700)




with aba3:
	st.header(abas[2])

	st.write('Aqui você tem acesso a tabela completa com todas as observações utilizadas nas outras dashboards. Cada linha representa uma entrada individual do conjunto de dados com os devidos filtros aplicados, contendo informações detalhadas sobre salários, setores, cargos, níveis de experiência e outros atributos relevantes.')
 
	st.divider()

	st.write(dados)

	st.download_button(label = '💾 Baixar Base de Dados Filtrada', 
						data = dados.to_csv(), 
						file_name='base-prof-dados-filtrada.csv', 
						mime='text/csv',    
						use_container_width=False)


	st.divider()

	st.write('Acesse a fonte dos dados no Kaggle: https://www.kaggle.com/datasets/datahackers/state-of-data-2021')
	st.write('Acesse o site do "State of Data" para relatórios mais recentes: http://www.stateofdata.com.br/')
	st.write('Conheça a equipe responsável por esse incrível levantamento de dados: https://www.datahackers.com.br/')



with aba4:
	st.header(abas[3])

	st.divider()

	st.subheader('1. Adicione uma opção para corrigir os valores do salário para valores atuais segundo algum índice financeiro (por exemplo, inflação)')

	st.divider()

	st.subheader('2. Adicione uma terceira aba para uma análise gráfica multivariada, na qual a pessoa pode escolher duas variáveis categóricas e visualizar um gráfico de barras agrupadas com o salário em cada barra. Por exemplo, Salário por Modelo de Trabalho e Nível.')

	st.divider()

	st.subheader('3. Adicione uma opção para que o usuário possa adicionar uma variável categórica adicional para filtragem. Ele deve decidir se deseja ou não adicionar outra variável. Se optar por adicionar, ele deve selecionar a variável na lista de variáveis categóricas relevantes. Depois de escolher a variável categórica, ele deve selecionar a categoria pela qual deseja filtrar o conjunto de dados.')


