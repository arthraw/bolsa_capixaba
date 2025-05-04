from pyspark.sql import DataFrame

def rename_cols(df: DataFrame) -> DataFrame:
    """
    Rename columns in dataframe

    :param df:
    :return df:
    """

    cols_rename = {
        "Ano": "year_benefit",
        "CodigoNIS": "nis",
        "NomeBeneficiario": "beneficiary_name",
        "DataReferencia": "reference_date",
        "ValorBeneficioComp": "benefit_value",
        "Municipio": "city",
        "CodIBGE": "ibge_code",
        "Situacao": "status",
        "Id": "source_id"
    }

    for old_col, new_col in cols_rename.items():
        df = df.withColumnRenamed(old_col, new_col)

    return df