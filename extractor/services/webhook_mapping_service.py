import json
from asyncio import Queue

from extractor.mappers.mapper_factory import mapper_factory
from extractor.repositories.sqlite_repository import document_processed, is_batch_completed


async def map_transactions(data: str, queue: Queue):
    data_dict = json.loads(data)
    transactions = mapper_factory.get(data_dict['organization'], data_dict['statement_type']).map_transactions(data)
    await queue.put(transactions)
    document_processed(data_dict['document_id'])
    if is_batch_completed(data_dict['remote_id']):
        await queue.put('completed')
