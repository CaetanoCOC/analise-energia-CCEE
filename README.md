# 📊 Análise de Consumo de Energia Elétrica no Brasil (CCEE)

Este repositório apresenta uma análise exploratória e dashboard interativo do consumo de energia elétrica no Brasil, utilizando dados públicos fornecidos pela Câmara de Comercialização de Energia Elétrica (CCEE).

---

## 📁 Estrutura do Projeto

```bash
ccee-energy-consumption-analysis/
│
├── data/                  # Dados brutos
│   └── CCEE_BR_Data.csv   # Dataset principal
│
├── dashboard/             # Aplicação Streamlit
│   └── main.py            # Ponto de entrada do dashboard
│
├── scripts/               # Funções reutilizáveis
│   └── utils.py           # Carregamento e pré-processamento
│
├── notebooks/             # Análises exploratórias em Jupyter
│   └── dados.ipynb        # Notebook inicial
│
├── outputs/               # Gráficos e tabelas geradas (opcional)
│
├── .gitignore             # Ignorar ambientes, caches, etc.
├── pyproject.toml         # Configuração do Poetry
└── README.md              # Documentação (este arquivo)
```

---

## 💾 Dataset

* **Fonte:** Câmara de Comercialização de Energia Elétrica (CCEE)
* **Arquivo:** `data/CCEE_BR_Data.csv`
* **Descrição:** Registros diários de consumo de energia por classe de consumidor, ramo de atividade, submercado, UF e indicador de período Covid.

---

## 🛠 Tecnologias e Bibliotecas

* **Python 3.12.5**
* **Gerenciamento de Ambiente:** Poetry + pyenv
* **Análise de Dados:** pandas, numpy
* **Visualização:** matplotlib, seaborn, plotly
* **Dashboard Interativo:** Streamlit
* **Jupyter Notebooks:** jupyter, ipykernel

---

## 🚀 Passo a Passo para Executar o Projeto

1. **Clone este repositório**

   ```bash
   git clone https://github.com/CaetanoCOC/analise-energia-CCEE.git
   cd analise-energia-CCEE
   ```

2. **Instale as dependências**

   ```bash
   poetry install
   ```

3. **Adicionar o dataset**

   * Verifique se o arquivo `CCEE_BR_Data.csv` está na pasta `data/`.

4. **Executar Análise Exploratória (opcional)**

   * Abra `notebooks/dados.ipynb` no VSCode ou Jupyter.

5. **Rodar o Dashboard**

   ```bash
   # Com Poetry:
   poetry run streamlit run dashboard/main.py

   # Ou, ativando o shell:
   poetry shell
   streamlit run dashboard/main.py
   ```

6. **Acessar no navegador**

   * Abra `http://localhost:8501` no seu navegador.

---

## 📋 O que foi feito

1. **Carregamento de Dados:** Leitura do CSV e conversão de colunas de data.
2. **Limpeza e Pré-processamento:** Renomeação de colunas, tratamento de tipos e criação de colunas auxiliares (ano e mês).
3. **Exploração Inicial:** Verificação de nulos, estatísticas descritivas e amostras do dataset.
4. **Dashboard Interativo em Streamlit:**

   * Filtros dinâmicos: ano, classe de consumidor, ramo de atividade, submercado, UF e período Covid.
   * KPIs principais: consumo total, média de consumo, anos filtrados.
   * Gráficos:

     * Linha de consumo total por ano.
     * Barras de consumo médio mensal.
     * Top 5 estados por consumo no ano mais recente.
     * Heatmap de consumo médio por ano e mês.
   * Tabela interativa de resumo anual.

---

## 📈 Resultados e Insights

* Identificação de padrões sazonais no consumo (meses mais e menos demandados).
* Comparação entre classes de consumidores e ramos de atividade.
* Evolução do consumo antes e após o pandemia.
* Benchmarking por estado (top 5 consumidores).

> **Dica para Recrutadores:** Navegue pela sidebar para testar diferentes recortes e explorar os dados.

---

## 🎯 Próximos Passos

* Incluir mapas choropleth por UF.
* Adicionar análise de séries temporais avançada (forecast).
* Publicar o dashboard online (Streamlit Cloud ou Heroku).

---

## 📄 Licença

Este projeto está licenciado sob a [MIT License](LICENSE).

---

> Desenvolvido por **Bruno Caetano** • [LinkedIn](https://www.linkedin.com/in/bcaetano-datascience/) • [GitHub](https://github.com/CaetanoCOC/analise-energia-CCEE)
