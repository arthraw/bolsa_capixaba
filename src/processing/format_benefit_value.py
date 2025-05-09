from pyspark.sql import DataFrame
from pyspark.sql.functions import udf
from pyspark.sql.types import IntegerType


def benefit_to_money_value(value: str):
    """
    Split original money value and convert to integer

    :param value:
    :return int/None:
    """

    if value:
        value_splt = value.split(',')
        result = value_splt[0]
        try:
            return int(result)
        except ValueError:
            return None
    return None


def format_benefit_value(df : DataFrame) -> DataFrame:
    """
    Apply formating function to benefit value

    :param df:
    :return df:
    """
    benefit_udf = udf(benefit_to_money_value, IntegerType())
    df = df.withColumn('benefit_value', benefit_udf(df['benefit_value']))
    return df