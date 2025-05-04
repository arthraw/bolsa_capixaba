import os
from src.utils.create_spark_instance import create_spark_instance
from src.processing.rename_cols import rename_cols
from src.processing.cast_col_types import cast_col_types
from src.processing.format_benefit_value import format_benefit_value
from src.utils.variables import silver_path, bronze_path
import logging
from src.utils import log

logger = logging.getLogger(__name__)


cleaning_process = {
    'first_step' : rename_cols,
    'second_step' : cast_col_types,
    'thirst_step' : format_benefit_value
}

def process_data(directory_path: str) -> None:
    spark = create_spark_instance()
    for file in os.listdir(directory_path):
        file_path = os.path.join(directory_path, file)

        if file.endswith(".csv"):
            df = spark.read.csv(file_path, header=True, inferSchema=False, sep=';')
        elif file.endswith(".parquet"):
            df = spark.read.parquet(file_path)
        elif file.endswith("json"):
            df = spark.read.json(file_path)
        else:
            logger.error(f"File type {file.split('.')[-1]} not supported.")
            continue

        for step, func in cleaning_process.items():
            try:
                logger.info(f"Running step: {step}")
                df = func(df)
                logger.info(f"Columns after step '{step}': {df.columns}")
            except Exception as e:
                logger.error(f"Error in step '{step}' for file '{file}': {e}")
                break
        file_base = os.path.splitext(file)[0]
        output_path = os.path.join(silver_path, file_base)
        df.write \
        .mode('overwrite') \
        .partitionBy("year_benefit", "month_benefit") \
        .parquet(output_path)
    logger.info(f"Cleaning raw (bronze) data process finished.")
    logger.info(f"Change data layer to silver.")

process_data(bronze_path)