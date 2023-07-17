import streamlit as st 

st.set_page_config(page_title="Escrita Markdown",
				   page_icon = "📜")



st.title('📜 Escrita Markdown')

st.markdown('# Escrita Markdown')

st.write('# Escrita Markdown')

'''
# Escrita Markdown - Título 1

## Escrita Markdown - Título 2

### Escrita Markdown - Título 3

#### Escrita Markdown - Título 4

##### Escrita Markdown - Título 5

###### Escrita Markdown - Título 6

Escrita normal 

---

## Formatação de Texto

Parágrafos são escritos normalmente. Não requer nenhuma codificação extra.
Para pular linhas, é necessário deixar uma linha vazia no local.


Para começar um novo parágrafo, basta dar um 'enter' a mais.

*Escrita em itálico*

**Escrita em negrito**

***Escrita em itálico e negrito***

~~Escrita riscada~~

---

## Listas

1. Primeiro Item
2. Segundo Item
2. Terceiro Item
1. Quarto Item
	1. Sublista
	2. Sublista

- Primeiro Item
- Segundo Item
- Terceiro Item
- Quarto Item
	- Sublista
	- Sublista

1. [ ] Tarefa 1
2. [x] Tarefa 2
3. [ ] Tarefa 3

- [ ] Tarefa 1
- [x] Tarefa 2
- [ ] Tarefa 3

---

## Tabelas

Coluna 1 | Coluna 2 | Coluna 3 | Coluna 4
--- | -----: | :---- | :-----:
A  |  1  |  Alice  |  Churrasco
B  |  2  |  Beto   |  Lasanha
C  |  3  |  Carla  |  Parmegiana

---

## Links

Site com a documentação do [Markdown](https://www.markdownguide.org/ "Documentação Oficial") 

https://www.markdownguide.org/

---

## Frase Destacada 

> Frase em destaque

---

## Emojis

🎈:fire:🌌

[Emojis Markdown](https://gist.github.com/rxaviers/7360908)

---

## Latex

Linguagem científica matemática.

$$ \int_a^b f(x)dx = F(b) - F(a)$$ 

https://www.latex-project.org/

---

'''

