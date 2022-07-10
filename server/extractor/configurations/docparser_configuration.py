import pydocparser

from transaction_collation.settings import ENV_DOCPARSER_API_KEY


def make_pdf_parser():
    parser = pydocparser.Parser()
    parser.login(ENV_DOCPARSER_API_KEY)
    assert parser.ping() == 'pong'
    return parser
