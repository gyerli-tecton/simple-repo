from tecton import batch_feature_view, FilteredSource, materialization_context
from ds.txn import txn_batch
from entities import user
from datetime import datetime, timedelta


# w/o using FilteredSource
@batch_feature_view(
    sources=[txn_batch],
    entities=[user],
    mode='spark_sql',
    online=True,
    offline=True,
    feature_start_time=datetime(2023, 8, 1),
    batch_schedule=timedelta(days=1),
    incremental_backfills=True,
    owner='gursoy@tecton.ai',
    ttl=timedelta(days=365)
)
def user_transaction_count_7d(txn, context=materialization_context()):
    return f'''
        SELECT
            user_id,
            count(transaction_id) as cnt,
            TO_TIMESTAMP("{context.end_time}") - INTERVAL 1 MICROSECOND as timestamp
        FROM
            {txn}
        WHERE timestamp >= TO_TIMESTAMP("{context.start_time}") - INTERVAL 6 DAY
          AND timestamp <= TO_TIMESTAMP("{context.end_time}")
        GROUP BY user_id
        '''

# # w/ using FilteredSource
# @batch_feature_view(
#     sources=[FilteredSource(txn_batch, start_time_offset=timedelta(days=-2))],
#     entities=[user],
#     mode='spark_sql',
#     online=True,
#     offline=True,
#     feature_start_time=datetime(2023, 8, 1),
#     batch_schedule=timedelta(days=1),
#     incremental_backfills=True,
#     owner='gursoy@tecton.ai',
#     ttl=timedelta(days=365)
# )
# def user_transaction_count_3d(txn, context=materialization_context()):
#     return f'''
#         SELECT
#             user_id,
#             count(transaction_id) as cnt,
#             TO_TIMESTAMP("{context.end_time}") - INTERVAL 1 MICROSECOND as timestamp
#         FROM
#             {txn}
#         GROUP BY user_id
#         '''



