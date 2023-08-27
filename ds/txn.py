from tecton import (
    FileConfig,
    HiveConfig,
    BatchSource,
    DatetimePartitionColumn
)

from datetime import datetime, timedelta

partition_columns = [
    DatetimePartitionColumn(column_name="partition_0", datepart="year", zero_padded=True),
    DatetimePartitionColumn(column_name="partition_1", datepart="month", zero_padded=True),
    DatetimePartitionColumn(column_name="partition_2", datepart="day", zero_padded=True),
]

hive_config = HiveConfig(
    database="gursoy_fraud_simple", 
    table="txn",
    timestamp_field="timestamp",
    datetime_partition_columns=partition_columns,
)

txn_batch = BatchSource(
    name="txn_batch",
    batch_config=hive_config,
    owner="gursoy@tecton.ai"
)