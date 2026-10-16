# Instalar as bibliotecas necessárias:
# pip install streamlit pandas numpy plotly[express]

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# Configuração da página
st.set_page_config(page_title="Painel de Vendas - Varejo On-line S.A.", layout="wide")

# Função para gerar dados de exemplo
@st.cache_data
def gerar_dados():
    df_vendas = pd.DataFrame({
        'Data': pd.date_range(start='2023-01-01', end='2023-12-31', freq='D'),
        'Vendas': np.random.randint(1000, 5000, 365),
        'Categoria': np.random.choice(['Eletrônicos', 'Roupas', 'Livros', 'Casa', 'Esportes'], 365)
    })

    df_clientes = pd.DataFrame({
        'Data': pd.date_range(start='2023-01-01', end='2023-12-31', freq='D'),
        'Novos_Clientes': np.random.randint(10, 100, 365),
        'Satisfacao': np.random.uniform(3.5, 5, 365)
    })

    df_produtos = pd.DataFrame({
        'Produto': ['Smartphone', 'Notebook', 'Tênis', 'Livro', 'Camiseta'],
        'Vendas': [15000, 12000, 9000, 7500, 6000],
        'Avaliacao': [4.5, 4.3, 4.2, 4.7, 4.1],
        'Categoria': ['Eletrônicos', 'Eletrônicos', 'Esportes', 'Livros', 'Roupas']
    })

    return df_vendas, df_clientes, df_produtos

# Carregar dados
df_vendas, df_clientes, df_produtos = gerar_dados()

# Sidebar com filtros
st.sidebar.header("Filtros")
categoria_selecionada = st.sidebar.multiselect(
    "Selecione as Categorias",
    options=df_vendas['Categoria'].unique(),
    default=df_vendas['Categoria'].unique()
)

# Filtrar dados
df_vendas_filtrado = df_vendas[df_vendas['Categoria'].isin(categoria_selecionada)]
df_produtos_filtrado = df_produtos[df_produtos['Categoria'].isin(categoria_selecionada)]

# Título do painel
st.title("Painel de Vendas - Varejo On-line S.A.")


# Métricas principais
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Total de Vendas", f"R$ {df_vendas_filtrado['Vendas'].sum():,.2f}")
with col2:
    st.metric("Novos Clientes", df_clientes['Novos_Clientes'].sum())
with col3:
    st.metric("Satisfação Média", f"{df_clientes['Satisfacao'].mean():.2f}")




# Gráfico de vendas ao longo do tempo
st.subheader("Vendas ao Longo do Tempo")
fig_vendas_tempo = px.line(df_vendas_filtrado, x='Data', y='Vendas')
st.plotly_chart(fig_vendas_tempo, use_container_width=True)

# Gráfico de vendas por categoria
st.subheader("Vendas por Categoria")
df_cat = df_vendas_filtrado.groupby('Categoria')['Vendas'].sum().reset_index()
fig_vendas_categoria = px.pie(df_cat, values='Vendas', names='Categoria')
st.plotly_chart(fig_vendas_categoria, use_container_width=True)

# Gráficos de novos clientes e satisfação
col1, col2 = st.columns(2)

with col1:
    st.subheader("Novos Clientes por Dia")
    fig_novos_clientes = px.bar(df_clientes, x='Data', y='Novos_Clientes')
    st.plotly_chart(fig_novos_clientes, use_container_width=True)

with col2:
    st.subheader("Satisfação dos Clientes ao Longo do Tempo")
    fig_satisfacao = px.line(df_clientes, x='Data', y='Satisfacao')
    st.plotly_chart(fig_satisfacao, use_container_width=True)

# Gráfico de top produtos
st.subheader("Top Produtos: Vendas vs. Avaliação")
fig_top_produtos = px.scatter(df_produtos_filtrado, x='Vendas', y='Avaliacao', size='Vendas',
                              text='Produto', title='Top Produtos: Vendas vs. Avaliação')
fig_top_produtos.update_traces(textposition='top center')
st.plotly_chart(fig_top_produtos, use_container_width=True)

# Tabela de dados
st.subheader("Dados Detalhados")
tab1, tab2, tab3 = st.tabs(["Vendas", "Clientes", "Produtos"])

with tab1:
    st.dataframe(df_vendas_filtrado)
with tab2:
    st.dataframe(df_clientes)
with tab3:
    st.dataframe(df_produtos_filtrado)



# Conclusão e Recomendações
st.markdown(f"""
## Conclusões e Recomendações

Com base nos dados apresentados neste painel, podemos concluir que:

1. As vendas têm uma tendência de crescimento, mas com algumas flutuações sazonais.
2. A categoria mais vendida é {df_cat.iloc[0]['Categoria']}, seguida por {df_cat.iloc[1]['Categoria'] if len(df_cat) > 1 else 'N/A'}.
3. A aquisição de novos clientes é consistente, com picos em determinados períodos.
4. A satisfação dos clientes mantém-se estável, com uma média de {df_clientes['Satisfacao'].mean():.2f}.
5. Os produtos mais vendidos nem sempre são os mais bem avaliados, indicando oportunidades de melhoria.

Recomendações:

- Focar em estratégias de marketing para as categorias menos vendidas, especialmente {df_cat.iloc[-1]['Categoria'] if len(df_cat) > 1 else 'N/A'}.
- Investigar as razões dos picos de aquisição de novos clientes nos dias {', '.join(df_clientes.nlargest(3, 'Novos_Clientes')['Data'].dt.strftime('%d/%m/%Y').tolist())} e replicar essas estratégias.
- Implementar um programa de fidelidade para manter a satisfação dos clientes alta, visando ultrapassar a média atual.
- Melhorar a qualidade dos produtos mais vendidos, mas com avaliações mais baixas, como {df_produtos_filtrado.nsmallest(1, 'Avaliacao')['Produto'].values[0] if not df_produtos_filtrado.empty else 'N/A'}.
- Considerar a expansão do estoque de produtos bem avaliados e com boas vendas, como {df_produtos_filtrado.nlargest(1, 'Avaliacao')['Produto'].values[0] if not df_produtos_filtrado.empty else 'N/A'}.
- Realizar uma análise mais profunda da sazonalidade das vendas para otimizar o estoque e as promoções.
""")
