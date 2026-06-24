from pyspark.sql.functions import col, to_date

bronze_path = "/Volumes/workspace/default/etl-project-1/bronze/"
silver_path = "/Volumes/workspace/default/etl-project-1/silver/"

print("Starting Silver Layer Transformation...")

# Read from Bronze layer
df_bronze = spark.read.format("delta").load(bronze_path)

# Data Cleaning & Transformation
df_silver = df_bronze.dropDuplicates(["order_id"]) \
                     .dropna(subset=["order_id", "product_category", "price"]) \
                     .withColumn("order_date", to_date(col("order_date"), "yyyy-MM-dd"))
                     
# Write to Silver layer with partitioning (No manual .cache() needed on Serverless!)
df_silver.write.format("delta") \
         .mode("overwrite") \
         .partitionBy("product_category") \
         .save(silver_path)
         
print(f"Silver transformation complete.")

# View the partitioned data
display(spark.read.format("delta").load(silver_path))