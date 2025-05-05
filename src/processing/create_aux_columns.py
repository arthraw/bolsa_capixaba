from pyspark.sql import DataFrame
from pyspark.sql.functions import lit


def create_aux_columns(df: DataFrame) -> DataFrame:
    """
    Create auxiliary columns for analysis

    :param df:
    :return df:
    """
    df_aux = df.withColumn('uf', lit('ES'))
    return df_aux