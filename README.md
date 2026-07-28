# ingestao-dados-gov

# Pipeline de Ingestão de Dados: Portal de Dados Abertos 

Este repositório contém a estrutura de um pipeline de Engenharia de Dados desenvolvido para automatizar a ingestão de planilhas governamentais (Folha de Pagamento/Bolsa Atleta) no Data Lake, construído na plataforma Databricks.

## Objetivo do Projeto
Coletar dados brutos em formato .xlsx do Portal de Dados Abertos, salvar os dados na camada Bronze garantindo rastreabilidade de ingestão, e em seguida, aplicar transformações, padronização e tipagem para disponibilizar os dados refinados na camada Silver do Data Lake, utilizando o formato Delta Lake.

## Tecnologias Utilizadas
* **Apache Spark / PySpark:** Processamento distribuído e transformação de dados.
* **Pandas:** Leitura e conversão de arquivos de origem.
* **Databricks:** Ambiente de desenvolvimento e orquestração.
* **Delta Lake:** Formato de armazenamento otimizado, utilizando operações de *append*.

## Arquitetura e Regras de Negócio
Camada Bronze:
O script src/bronze_gov_folha_pagamento.py executa as seguintes etapas:
Ingestão: Leitura do arquivo Excel original da fonte.
Sanitização de Tipagem: Conversão forçada de todas as colunas de negócio para o tipo string, evitando quebras por inferência incorreta de schema.
Auditoria: Inserção de metadados essenciais para governança:
_ingested_at: Timestamp exato da carga.
_source_table: Tabela ou arquivo de origem lógica.
_source_system: Sistema de origem (ex: Planilha).
Armazenamento: Gravação no formato Delta em modo append.

Camada Silver:
O script src/silver_tratamento_pagamentos.py executa as seguintes etapas:
Padronização: Renomeação das colunas originais para o padrão snake_case (sem espaços ou caracteres especiais).
Tipagem Avançada (Cast): Conversão dos dados de string para os formatos analíticos corretos (ex: DoubleType para valores de bolsas, DateType para datas).
Limpeza e Qualidade: Remoção de espaços vazios indesejados (trim) nos campos de texto.
Armazenamento: Gravação no formato Delta em modo overwrite, mantendo a base tratada atualizada para consumo.

## Orquestração
A automação da rotina é definida como Código (Infrastructure as Code) utilizando *Databricks Asset Bundles / Jobs YAML*. A rotina está configurada em `jobs/databricks_job.yml` para execução diária via CRON (`0 0 2 * * ?`).
