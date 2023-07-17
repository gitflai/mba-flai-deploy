import streamlit as st 

st.set_page_config(page_title="Imagens, Áudios e Vídeos",
				   page_icon = "📺")


st.title('📺 Imagens, Áudios e Vídeos')


st.header('Forma Local')

st.image('recursos/exemplo_imagem.jpg')
st.audio('recursos/exemplo_som.mp3')
st.video('recursos/exemplo_video.mp4')


st.header('Forma Online')

st.image('https://github.com/ricardorocha86/arquivos/blob/main/exemplo_imagem.jpg?raw=true')
st.audio('https://github.com/ricardorocha86/arquivos/raw/main/exemplo_som.mp3')
st.video('https://github.com/ricardorocha86/arquivos/raw/main/exemplo_video.mp4')