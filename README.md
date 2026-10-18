# Python com Spark

Repositório de atividades da disciplina **Linguagens de Programação para Ciência de Dados**, organizadas por tema. Cada seção abaixo aponta para a pasta correspondente e resume os conteúdos, ferramentas e arquivos de dados utilizados.

## Temas

### [Tema 1 — Python e bibliotecas para análise de dados](./Tema%201/)

Fundamentos da linguagem Python, manipulação de dados tabulares, limpeza de dados e visualização.

- **Bloco 1:** coleta, processamento e limpeza de dados de vendas com [Pandas](./Tema%201/Tema_1_Bloco_1.ipynb).
- **Bloco 2:** tipos de dados, variáveis, operadores, listas e dicionários em [Python](./Tema%201/Tema_1_Bloco_2.ipynb).
- **Bloco 3:** operações com [NumPy](./Tema%201/Tema_1_Bloco_3.ipynb), DataFrames e estatística descritiva com Pandas, além de gráficos com [Matplotlib e Seaborn](./Tema%201/Tema_1_Bloco_3.ipynb).
- **Bloco 4:** criação de dados sintéticos de e-commerce com NumPy e Pandas e exportação para CSV ([notebook](./Tema%201/Tema_1_Bloco_4.ipynb)).
- **Dados:** [`vendas.csv`](./Tema%201/vendas.csv), [`vendas_processadas.csv`](./Tema%201/vendas_processadas.csv) e [`vendas_ecommerce.csv`](./Tema%201/vendas_ecommerce.csv).

### [Tema 2 — Big Data e Apache Spark](./Tema%202/)

Introdução ao processamento distribuído com Apache Spark, explorando RDDs, Spark SQL, DataFrames e aprendizado de máquina.

- [Demonstração de RDD](./Tema%202/Tema_2_Bloco_3_demonstra%C3%A7%C3%A3o.ipynb): leitura de vendas, transformações e agregações com `SparkContext` e RDDs.
- [Demonstração de Spark SQL](./Tema%202/Tema_2_Bloco_3_demonstra%C3%A7%C3%A3o_SQL.ipynb): criação de DataFrames, views temporárias, consultas SQL e funções de agregação.
- [Demonstração de MLlib](./Tema%202/Tema_2_Bloco_3_demonstra%C3%A7%C3%A3o_RDD.ipynb): preparação de atributos, classificação por regressão logística e avaliação do modelo.
- **Recursos:** PySpark, `SparkContext`, `SparkSession`, RDD, DataFrame, Spark SQL e Spark MLlib (`VectorAssembler`, `LogisticRegression` e `BinaryClassificationEvaluator`).

### [Tema 3 — Análise de dados com PySpark](./Tema%203/)

Leitura e transformação de dados estruturados, análise de vendas, clientes e estoque, e construção de um modelo preditivo.

- [Bloco 1](./Tema%203/Tema_3_Bloco_1.ipynb): leitura de CSV e JSON, inspeção de esquemas, filtros e agregações com DataFrames.
- [Bloco 2](./Tema%203/Tema_3_Bloco_2.ipynb): geração e análise de dados de vendas, comportamento de clientes e estoque.
- [Bloco 3](./Tema%203/Tema_3_Bloco_3.ipynb): pipeline de aprendizado de máquina para estimar nível de glicose com Random Forest.
- **Recursos:** PySpark SQL/DataFrames, funções e tipos do Spark, leitura de CSV/JSON, PySpark MLlib, `VectorAssembler`, `StandardScaler`, `Pipeline`, `RandomForestRegressor` e `RegressionEvaluator`.
- **Dados:** [`vendas.csv`](./Tema%203/vendas.csv), [`clientes.json`](./Tema%203/clientes.json), [`dados_vendas.csv`](./Tema%203/dados_vendas.csv), [`comportamento_cliente.json`](./Tema%203/comportamento_cliente.json), [`dados_estoque.csv`](./Tema%203/dados_estoque.csv) e [`pacientes_diabetes.csv`](./Tema%203/pacientes_diabetes.csv).

### [Tema 4 — Dashboards e visualização interativa](./Tema%204/)

Aplicações para explorar indicadores e gráficos interativos em dashboards.

- [Streamlit — dashboard de exemplo](./Tema%204/Tema_4_Streamlit1.py) e [painel de vendas](./Tema%204/Tema_4_Streamlit2.py).
- [Plotly Dash](./Tema%204/Tema_4_PlotlyDash.py) e [Plotly Dash com callback](./Tema%204/Tema_4_PlotlyDash_callback.py).
- **Recursos:** Streamlit, Dash, Plotly Express, Pandas e NumPy. Os exemplos criam dados de vendas, clientes e produtos para exibir métricas, filtros e gráficos.
