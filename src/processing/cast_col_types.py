from pyspark.sql.connect.dataframe import DataFrame
from pyspark.sql.functions import col, to_date, month


def cast_col_types(df: DataFrame) -> DataFrame:
    """
    Cast all data types in dataframe

    :param df:
    :return df:
    """
    cols_cast = {
        "year_benefit": "int",
        "nis": "string",
        "beneficiary_name": "string",
        "reference_date": "string",
        "benefit_value": "string",
        "city": "string",
        "ibge_code": "string",
        "status": "string",
        "uf" : "string"
    }

    for column, col_type in cols_cast.items():
        df = df.withColumn(column, col(column).cast(col_type))

    df_cast = df.withColumn(
        "reference_date",
        to_date("reference_date", "dd/MM/yyyy HH:mm:ss")
    )
    df_cast = df_cast.withColumn("month_benefit", month(col("reference_date")))

    return df_cast