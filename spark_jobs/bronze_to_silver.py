from pathlib import Path
from pyspark.sql import SparkSession
from pyspark.sql.types import *
from pyspark.sql.functions import *

BASE_DIR = Path(__file__).resolve().parents[1]

bronze_path = str(BASE_DIR / "bronze" / "orders")
silver_path = str(BASE_DIR / "silver" / "orders")
checkpoint_path = str(BASE_DIR / "silver" / "checkpoint")

spark = SparkSession.builder \
    .appName("BronzeToSilver") \
    .master("local[*]") \
    .getOrCreate()

spark.sparkContext.setLogLevel("WARN")

# Bronze CSV has one column: JSON string from Kafka
raw_schema = StructType([
    StructField("json_value", StringType(), True)
])

# Actual order schema inside JSON
order_schema = StructType([
    StructField("OrderID", IntegerType(), True),
    StructField("CustomerID", IntegerType(), True),
    StructField("ProductID", IntegerType(), True),
    StructField("Quantity", IntegerType(), True),
    StructField("Price", IntegerType(), True),
    StructField("City", StringType(), True),
    StructField("OrderTime", StringType(), True)
])

df = spark.readStream \
    .format("csv") \
    .option("header", "false") \
    .schema(raw_schema) \
    .load(bronze_path)

clean_df = df.select(
    from_json(col("json_value"), order_schema).alias("data")
).select("data.*")

clean_df = clean_df.na.drop()

clean_df = clean_df.withColumn(
    "OrderTime",
    to_timestamp(col("OrderTime"), "yyyy-MM-dd HH:mm:ss")
)

query = clean_df.writeStream \
    .format("csv") \
    .option("header", "true") \
    .option("path", silver_path) \
    .option("checkpointLocation", checkpoint_path) \
    .outputMode("append") \
    .start()

print("===== Bronze to Silver streaming started =====")
print("Reading from:", bronze_path)
print("Writing to:", silver_path)

query.awaitTermination()