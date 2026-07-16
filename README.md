# ingestao-dados-gov

# Pipeline de Ingestão de Dados: Portal de Dados Abertos 📊

Este repositório contém a estrutura de um pipeline de Engenharia de Dados desenvolvido para automatizar a ingestão de planilhas governamentais (Folha de Pagamento/Bolsa Atleta) no Data Lake, construído na plataforma **Databricks**.

## Objetivo do Projeto
Coletar dados brutos em formato `.xlsx` do Portal de Dados Abertos, aplicar validações de tipagem e salvar os dados na camada **Bronze** do Data Lake utilizando o formato **Delta Lake**, garantindo rastreabilidade e governança.

## Tecnologias Utilizadas
* **Apache Spark / PySpark:** Processamento distribuído e transformação de dados.
* **Pandas:** Leitura e conversão de arquivos de origem.
* **Databricks:** Ambiente de desenvolvimento e orquestração.
* **Delta Lake:** Formato de armazenamento otimizado, utilizando operações de *append*.

## Arquitetura e Regras de Negócio
O script `src/bronze_gov_folha_pagamento.py` executa as seguintes etapas:
1. **Ingestão:** Leitura do arquivo Excel original da fonte.
2. **Sanitização de Tipagem:** Conversão forçada de todas as colunas de negócio para o tipo `string`, evitando quebras por inferência incorreta de schema.
3. **Auditoria:** Inserção de metadados essenciais para governança:
   * `_ingested_at`: Timestamp exato da carga.
   * `_source_table`: Tabela ou arquivo de origem lógica.
   * `_source_system`: Sistema de origem (ex: Planilha).
4. **Armazenamento:** Gravação no formato Delta em modo `append`.

## Orquestração
A automação da rotina é definida como Código (Infrastructure as Code) utilizando *Databricks Asset Bundles / Jobs YAML*. A rotina está configurada em `jobs/databricks_job.yml` para execução diária via CRON (`0 0 2 * * ?`).
