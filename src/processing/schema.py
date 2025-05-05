from pyspark.sql.types import StructType, StructField, StringType, IntegerType, DateType

expected_schema = StructType([
    StructField("year_benefit", IntegerType(), True),
    StructField("nis", StringType(), True),
    StructField("beneficiary_name", StringType(), True),
    StructField("reference_date", DateType(), True),
    StructField("benefit_value", IntegerType(), True),
    StructField("city", StringType(), True),
    StructField("ibge_code", StringType(), True),
    StructField("status", StringType(), True),
    StructField("uf", StringType(), True),
])
