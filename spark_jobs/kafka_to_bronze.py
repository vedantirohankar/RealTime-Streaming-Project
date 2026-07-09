from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .master("local[*]") \
    .appName("KafkaToBronze") \
    .getOrCreate()

spark.sparkContext.setLogLevel("INFO")

print("===== Spark Started =====")

df = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "orders") \
    .option("startingOffsets", "latest") \
    .load()

print("===== Kafka Connected =====")

json_df = df.selectExpr("CAST(value AS STRING)")

query = json_df.writeStream \
    .format("csv") \
    .option("path", "../bronze/orders") \
    .option("checkpointLocation", "../bronze/checkpoint") \
    .outputMode("append") \
    .start()

print("===== Streaming Started =====")

query.awaitTermination()