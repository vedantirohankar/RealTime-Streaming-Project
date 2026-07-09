from pyspark.sql import SparkSession
from pyspark.sql.types import *
from pyspark.sql.functions import *

spark = SparkSession.builder \
    .appName("SilverToGold") \
    .getOrCreate()

schema = StructType([
    StructField("OrderID", IntegerType(), True),
    StructField("CustomerID", IntegerType(), True),
    StructField("ProductID", IntegerType(), True),
    StructField("Quantity", IntegerType(), True),
    StructField("Price", IntegerType(), True),
    StructField("City", StringType(), True),
    StructField("OrderTime", TimestampType(), True)
])

df = spark.read \
    .option("header", "true") \
    .schema(schema) \
    .csv(r"C:\Users\ASUS\Downloads\RealTime-streaming\silver\orders")

gold_df = df.groupBy("City").agg(
    count("*").alias("TotalOrders"),
    sum("Price").alias("Revenue"),
    avg("Price").alias("AverageOrderValue")
)

gold_df.write \
    .mode("overwrite") \
    .option("header", "true") \
    .csv(r"C:\Users\ASUS\Downloads\RealTime-streaming\gold\orders") 

print("Gold layer created successfully")
   

