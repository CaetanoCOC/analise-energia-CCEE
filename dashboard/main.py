# dashboard

import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

# ——— 1) Construção do caminho até o CSV ———
BASE = Path(__file__).parent.parent   # dashboard/ → projeto raiz
DATA_PATH = BASE / "data" / "CCEE_BR_Data.csv"

@st.cache_data
def load_data(path: Path) -> pd.DataFrame:
    df = pd.read_csv(path)
    # limpeza e pré-processamento
    df['Data'] = pd.to_datetime(df['Data'], dayfirst=True, format='%d/%m/%Y')
    df = df.rename(columns={
        'Classe': 'classe_consumidor',
        'Ramo': 'ramo_atividade',
        'Submercado': 'regiao',
        'UF': 'estado',
        'Consumo': 'consumo_mwh',
        'Covid': 'indicador_covid'
    })
    df['ano'] = df['Data'].dt.year
    df['mes'] = df['Data'].dt.month
    return df

# ——— 2) Configurações da página ———
st.set_page_config(page_title="Dashboard Consumo CCEE", layout="wide")
st.title("🔌 Consumo de Energia Elétrica no Brasil (CCEE)")

# ——— 3) Carregar os dados ———
df = load_data(DATA_PATH)

# ——— 4) Filtros na sidebar ———
st.sidebar.header("Filtros")
anos = sorted(df['ano'].unique())
sel_anos = st.sidebar.multiselect("Ano", anos, default=anos)

classes = sorted(df['classe_consumidor'].unique())
sel_classes = st.sidebar.multiselect("Classe de Consumidor", classes, default=classes)

ramos = sorted(df['ramo_atividade'].unique())
sel_ramos = st.sidebar.multiselect("Ramo de Atividade", ramos, default=ramos)

regioes = sorted(df['regiao'].unique())
sel_regioes = st.sidebar.multiselect("Região/Submercado", regioes, default=regioes)

covid_vals = sorted(df['indicador_covid'].unique())
covid_map = {0: 'Pré-Covid', 1: 'Pós-Covid'}
sel_covid = st.sidebar.multiselect(
    "Período Covid",
    options=covid_vals,
    format_func=lambda x: covid_map[x],
    default=covid_vals
)

# Aplica filtros
mask = (
    df['ano'].isin(sel_anos) &
    df['classe_consumidor'].isin(sel_classes) &
    df['ramo_atividade'].isin(sel_ramos) &
    df['regiao'].isin(sel_regioes) &
    df['indicador_covid'].isin(sel_covid)
)
df_filtrado = df.loc[mask]


# ——— 5) Métricas (KPIs) ———
c1, c2, c3 = st.columns(3)
total_consumo = df_filtrado['consumo_mwh'].sum()
media_consumo = df_filtrado['consumo_mwh'].mean()
anos_filtrados = df_filtrado['ano'].nunique()
c1.metric("Consumo Total (MWh)", f"{total_consumo:,.0f}")
c2.metric("Média de Consumo (MWh)", f"{media_consumo:,.0f}")
c3.metric("Anos Filtrados", f"{anos_filtrados}")

# ——— 6) Gráfico 1: Consumo Total por Ano ———
consumo_anual = (
    df_filtrado.groupby('ano')['consumo_mwh']
    .sum()
    .reset_index()
)
fig1 = px.line(
    consumo_anual, x='ano', y='consumo_mwh',
    labels={'ano':'Ano', 'consumo_mwh':'MWh'},
    title="Consumo Total por Ano"
)
st.plotly_chart(fig1, use_container_width=True)

# ——— 7) Gráfico 2: Consumo Médio Mensal ———
sazonal = (
    df_filtrado.groupby('mes')['consumo_mwh']
    .mean()
    .reset_index()
)
fig2 = px.bar(
    sazonal, x='mes', y='consumo_mwh',
    labels={'mes':'Mês', 'consumo_mwh':'MWh'},
    title="Consumo Médio Mensal"
)
st.plotly_chart(fig2, use_container_width=True)

# ——— 8) Gráfico 3: Top 5 Estados no Ano Mais Recente ———
if sel_anos:
    latest_year = max(sel_anos)
    top5 = (
        df_filtrado[df_filtrado['ano'] == latest_year]
        .groupby('estado')['consumo_mwh']
        .sum()
        .nlargest(5)
        .reset_index()
    )
    fig3 = px.bar(
        top5, x='estado', y='consumo_mwh',
        labels={'estado':'Estado', 'consumo_mwh':'MWh'},
        title=f"Top 5 Estados por Consumo em {latest_year}"
    )
    st.plotly_chart(fig3, use_container_width=True)

# ——— 9) Gráfico 4: Heatmap de Consumo Médio Ano vs Mês ———
pivot = (
    df_filtrado.pivot_table(
        index='ano', columns='mes', values='consumo_mwh', aggfunc='mean'
    )
)
fig4 = px.imshow(
    pivot, aspect='auto',
    labels=dict(x="Mês", y="Ano", color="MWh"),
    title="Heatmap de Consumo Médio por Ano e Mês"
)
st.plotly_chart(fig4, use_container_width=True)

# ——— 10) Tabela de Resumo ———
st.subheader("Resumo de Consumo Anual")
st.dataframe(
    consumo_anual.style.format({"consumo_mwh":"{:,.0f}"})
)