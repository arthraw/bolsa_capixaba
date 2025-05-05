from pyspark.sql import DataFrame
from pyspark.sql.types import StructType
from pyspark.sql.utils import AnalysisException
import logging
from src.utils import log

logger = logging.getLogger(__name__)


def validate_schema(df: DataFrame, expected_schema: StructType) -> bool:
    try:
        actual_fields = set((field.name, field.dataType.simpleString()) for field in df.schema.fields)
        expected_fields = set((field.name, field.dataType.simpleString()) for field in expected_schema.fields)

        missing = expected_fields - actual_fields
        extra = actual_fields - expected_fields

        if missing:
            raise ValueError(f"Missing fields: {missing}")
        if extra:
            logger.info(f"Warning: extra fields present: {extra}")
        logger.info(f"Schema validated. Number of fields: {len(actual_fields)}")
        return True

    except Exception as e:
        logger.error(f"Schema validation failed: {e}")
        return False
