from pyspark.sql.functions import sum, count, round, col

silver_path = "/Volumes/workspace/default/etl-project-1/silver/"
gold_path = "/Volumes/workspace/default/etl-project-1/gold/"

print("🚀 Starting Gold Layer Aggregation...")

# Read from Silver layer
df_silver = spark.read.format("delta").load(silver_path)

# Calculate revenue and aggregate by Category
df_gold = df_silver.withColumn("total_price", col("quantity") * col("price")) \
                   .groupBy("product_category") \
                   .agg(
                       count("order_id").alias("total_orders"),
                       round(sum("total_price"), 2).alias("total_revenue")
                   ) \
                   .orderBy(col("total_revenue").desc())
                   
# Write to Gold layer
df_gold.write.format("delta").mode("overwrite").save(gold_path)

print("Top Performing Categories (Gold Layer Analytics View):")
# Databricks native display will render this as a clean, interactive UI table!
display(df_gold)
