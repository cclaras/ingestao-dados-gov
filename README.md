## Arquitetura do Projeto

*   **Bronze:** Ingestão dos dados brutos do programa Bolsa Atleta do governo.
*   **Silver:** Limpeza, padronização de colunas (tipagem, renomeação) e remoção de duplicatas utilizando PySpark.
*   **Gold:** Modelagem dimensional em Star Schema (Esquema Estrela), dividida em:
    *   `dim_atleta`: Dimensão contendo os dados únicos dos beneficiários (CPF, Nome, Município, UF).
    *   `fato_pagamento`: Fato contendo as métricas e detalhes dos pagamentos recebidos.

## Modelagem de Dados
![Diagrama Dimensional](diagrama.png)

## Dashboard
Análise regional dos beneficiários do Bolsa Atleta, desenvolvida diretamente no Databricks.
![Dashboard Bolsa Atleta](dashboard.png)
