import asyncio
from asyncio import Queue

import pydocparser
from asgiref.sync import async_to_sync
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from extractor.services.webhook_mapping_service import map_transactions
from transaction_collation.settings import ENV_DOCPARSER_API_KEY

PROCESSED_FILE_QUEUE = Queue()


@csrf_exempt
@async_to_sync
async def docparser_webhook(request):
    if request.method == 'POST':
        loop = asyncio.get_running_loop()
        loop.create_task(map_transactions(request.body, PROCESSED_FILE_QUEUE))

        return HttpResponse('received', content_type='text/plain')


def test_docparser(request):
    parser = pydocparser.Parser()
    parser.login(ENV_DOCPARSER_API_KEY)
    print(parser.ping())
    data = parser.get_one_result('UOB Credit Card Parser', 'b4efa1224daf464b31bf76550af8a003')
    print(data)
    return HttpResponse('ok')
