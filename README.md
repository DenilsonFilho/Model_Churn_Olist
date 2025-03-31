# Modelo de Predição de Churn

Este repositório é dedicado aos meus estudos sobre **Machine Learning**, incluindo como treinar modelos e como transformar e processar dados para a criação de tabelas analíticas, utilizando **SQL** e **Python**. Esses estudos têm como fonte a playlist de Machine Learning do canal **Teomywhy**. Utilizei dados coletados de seu repositório **(dtona)**, que, por sua vez, são públicos e fornecidos por uma empresa de marketplace chamada **Olist**. 

### Sobre o Estudo
O foco do projeto é a predição de **churn** dos vendedores da Olist. Para este estudo, um vendedor é considerado churn se ele deixar de realizar compras nos três meses subsequentes ao mês da última compra.

### Passo seguidos

- Criação de um **book de variáveis** por meio de consultas SQL que acessam diretamente um banco de dados SQLite, onde estão armazenados os dados da Olist.
- Utilização do Python (com as bibliotecas **SQLAlchemy**, **os** e **pandas**) para acessar o banco SQLite e criar a tabela book de variáveis a partir da consulta desenvolvida no ponto anterior.
- Inclusão no book de variáveis de todas as safras disponíveis para a construção do modelo, **totalizando 15 safras**.
- Desenvolvimento de uma consulta SQL para vincular todo o book à variável resposta de churn, criando assim a primeira **Analytical Base Table (ABT)**. 
- Criação do algoritmo **DecisionTreeClassifier** (Árvore de Decisão), um modelo supervisionado de classificação, utilizando a biblioteca **Scikit-Learn**.
- Utilização da metodologia **OneHotEncoder** para adequar as variáveis categóricas ao treino do algoritimo.
- Divisão da ABT em conjuntos de treino, teste e **Out of Time (OOT)**, para treinar e testar a Árvore de Decisão. Além disso, o conjunto OOT foi utilizado para a validação final do modelo. 
