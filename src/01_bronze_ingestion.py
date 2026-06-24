from pyspark.sql.functions import current_timestamp

# Define Volume paths instead of local OS paths
raw_data_path = "/Volumes/workspace/default/etl-project-1/raw_sales.csv"
bronze_path = "/Volumes/workspace/default/etl-project-1/bronze/"

print("Starting Bronze Layer Ingestion...")

# Read raw CSV directly from the Volume
df_raw = spark.read.csv(raw_data_path, header=True, inferSchema=True)

# Add ingestion timestamp
df_bronze = df_raw.withColumn("ingestion_timestamp", current_timestamp())

# Write to Bronze layer in Delta format
df_bronze.write.format("delta").mode("overwrite").save(bronze_path)

print(f"Bronze ingestion complete.")
display(df_bronze)