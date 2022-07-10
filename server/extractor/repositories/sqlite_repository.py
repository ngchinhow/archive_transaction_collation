from extractor.models import Document


def document_processed(document_id: str):
    Document.objects.filter(id=document_id).update(processed=True)


def is_batch_completed(batch_id: str):
    return Document.objects.filter(processed=False, batch_id=batch_id).count() == 0
