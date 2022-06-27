import pydocparser
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from transaction_collation.settings import ENV_DOCPARSER_API_KEY


@csrf_exempt
def nanonets_webhook(request):
    if request.method == 'POST':
        print('data received from webhook: ', request.body)
        return HttpResponse('received')


def test_docparser(request):
    parser = pydocparser.Parser()
    parser.login(ENV_DOCPARSER_API_KEY)
    print(parser.ping())
    data = parser.get_one_result('UOB Credit Card Parser', 'b4efa1224daf464b31bf76550af8a003')
    print(data)
    return HttpResponse('ok')

