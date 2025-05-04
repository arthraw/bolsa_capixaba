from pyspark.sql import SparkSession

def create_spark_instance():
    spark = (
                SparkSession.builder
                .appName('BolsaCapixaba')
                .getOrCreate()
             )
    return spark