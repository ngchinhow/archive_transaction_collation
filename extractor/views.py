import asyncio
import json
from asyncio import Queue

import pydocparser
from asgiref.sync import async_to_sync
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from transaction_collation.settings import ENV_DOCPARSER_API_KEY

PROCESSED_FILE_QUEUE = Queue()


@csrf_exempt
@async_to_sync
async def docparser_webhook(request):
    # await long_sleep()
    loop = asyncio.get_running_loop()
    loop.create_task(long_sleep())
    if request.method == 'POST':
        print('data received from webhook: ', request.body)
        # request_dict = json.loads(request.body)
        # match request_dict['organization']:
        #     case 'UOB':
        #         match request_dict['statement_type']:
        #             case 'card':
        #                 pass
        #             case 'account':
        #                 pass
        #     case 'OCBC':
        #         pass
        #     case 'POSB':
        #         pass

        return HttpResponse('received', content_type='text/plain')


def test_docparser(request):
    parser = pydocparser.Parser()
    parser.login(ENV_DOCPARSER_API_KEY)
    print(parser.ping())
    data = parser.get_one_result('UOB Credit Card Parser', 'b4efa1224daf464b31bf76550af8a003')
    print(data)
    return HttpResponse('ok')


async def long_sleep():
    await asyncio.sleep(5)
    print('awaken!')
