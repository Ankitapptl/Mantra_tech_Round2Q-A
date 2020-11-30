#Completed

from pyspark import SparkContext
from pyspark.sql import SQLContext
from pyspark.sql.types import *


if __name__ == "__main__":
    sc = SparkContext(appName="CSV2Parquet")
    sqlContext = SQLContext(sc)
    
    schema = StructType([
            StructField("col1", IntegerType(), True),
            StructField("col2", IntegerType(), True),
            StructField("col3", StringType(), True)])
    
    rdd = sc.textFile("C:\Users\user\PycharmProjects\mycsv.csv").map(lambda line: line.split(","))
    df = sqlContext.createDataFrame(rdd, schema)
    df.write.parquet('C:\Users\user\PycharmProjects\mycsv-parquet')
