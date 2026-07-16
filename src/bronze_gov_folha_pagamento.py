import pandas as pd
from pyspark.sql.functions import current_timestamp, lit, col
from pyspark.sql.types import StringType

# caminho de origem do arquivo no ambiente do databricks 
caminho_arquivo = "/FileStore/tables/PDA202604___BolsaAtleta.xlsx" 

# 1. leitura do arquivo forçando o tipo string
pdf = pd.read_excel(caminho_arquivo, dtype=str)
df = spark.createDataFrame(pdf)

# 2. adição das colunas de controle de ingestão
df_bronze = df \
    .withColumn("_ingested_at", current_timestamp()) \
    .withColumn("_source_table", lit("workspace.gov.pda_202604_bolsa_atleta")) \
    .withColumn("_source_system", lit("Planilha"))

# 3. garantia final de conversão das colunas originais para String
for c in pdf.columns:
    df_bronze = df_bronze.withColumn(c, col(c).cast(StringType()))

# 4. ingestão no formato delta em modo append 
df_bronze.write \
    .format("delta") \
    .mode("append") \
    .saveAsTable("workspace.gov.pda_202604_bolsa_atleta")
