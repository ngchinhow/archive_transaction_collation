import asyncio
from asyncio import Queue

import pydocparser
from asgiref.sync import async_to_sync
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from extractor.services.webhook_mapping_service import handle_document
from transaction_collation.settings import ENV_DOCPARSER_API_KEY

PROCESSED_FILE_QUEUE = Queue()


@csrf_exempt
@async_to_sync
async def docparser_webhook(request):
    if request.method == 'POST':
        loop = asyncio.get_running_loop()
        loop.create_task(handle_document(request.body, PROCESSED_FILE_QUEUE))

        return HttpResponse('received', content_type='text/plain')


@csrf_exempt
def file_upload(request):
    print(request.FILES)
    for file in request.FILES.getlist('file'):
        print(file.read())
    return HttpResponse(status=204)
