from pyspark.sql.connect.dataframe import DataFrame
from pyspark.sql.functions import col, to_date, month


def cast_col_types(df: DataFrame) -> DataFrame:

    cols_cast = {
        "year_benefit": "int",
        "nis": "string",
        "beneficiary_name": "string",
        "reference_date": "string",
        "benefit_value": "string",
        "city": "string",
        "ibge_code": "string",
        "status": "string",
        "source_id": "int"
    }

    for column, col_type in cols_cast.items():
        df = df.withColumn(column, col(column).cast(col_type))

    df = df.withColumn(
        "reference_date",
        to_date("reference_date", "dd/MM/yyyy HH:mm:ss")
    )
    df = df.withColumn("month_benefit", month(col("reference_date")))

    return df