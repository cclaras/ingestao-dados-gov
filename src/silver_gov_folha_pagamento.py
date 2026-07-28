# Databricks notebook source
from pyspark.sql.functions import col, to_date

# 1. ler a tabela da camada Bronze
df_bronze = spark.table("workspace.gov.pda_202604_bolsa_atleta")

# 2. renomear colunas e ajustar tipos
df_tratado = df_bronze \
    .withColumnRenamed("Edital", "edital") \
    .withColumnRenamed("CPF", "cpf") \
    .withColumnRenamed("Nome do Atleta", "nome_atleta") \
    .withColumnRenamed("Categoria", "categoria") \
    .withColumnRenamed("Modalidade", "modalidade") \
    .withColumnRenamed("Situação", "situacao") \
    .withColumnRenamed("Valor Pago", "valor_pago") \
    .withColumnRenamed("Data de Pagamento", "data_pagamento") \
    .withColumnRenamed("Data de referência", "data_referencia") \
    .withColumnRenamed("Municipio", "municipio") \
    .withColumnRenamed("UF", "uf") \
    .withColumn("valor_pago", col("valor_pago").cast("double")) \
    .withColumn("data_pagamento", to_date(col("data_pagamento")))

# 3. salvar na camada Silver
df_tratado.write \
    .format("delta") \
    .mode("overwrite") \
    .saveAsTable("workspace.gov.silver_bolsa_atleta")

display(df_tratado)