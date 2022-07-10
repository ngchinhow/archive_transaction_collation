import json
from asyncio import Queue

from asgiref.sync import sync_to_async

from extractor.mappers.mapper_factory import mapper_factory
from extractor.repositories.sqlite_repository import document_processed, is_batch_completed


async def handle_document(data: str, queue: Queue):
    data_dict = json.loads(data)
    transactions = mapper_factory.get(data_dict['organization'], data_dict['statement_type'])\
                                 .map_transactions(data_dict)
    print(transactions)
    await queue.put(transactions)
    # sync_to_async(document_processed(data_dict['document_id']))
    # if sync_to_async(is_batch_completed(data_dict['batch_id'])):
    #     await queue.put('completed')
