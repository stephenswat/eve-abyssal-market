from django.db import transaction

from eve_mail_queue.models import Mail, MailRecipient


@transaction.atomic
def send_mail(subject, body, recipients, priority=None, sender=None):
    mail = Mail(
        sender=sender,
        subject=subject,
        body=body,
    )

    if priority is not None:
        mail.priority = priority

    mail.save()

    for r in recipients:
        if type(r) == int:
            rec_id = r
            rec_type = MailRecipient.TYPE_CHARACTER
        elif type(r) == tuple:
            rec_id, rec_type = r
        elif type(r) == dict:
            rec_id = r['id']
            rec_type = r.get('type', MailRecipient.TYPE_CHARACTER)
        else:
            raise ValueError('Invalid recipient input.')

        MailRecipient(
            mail=mail,
            recipient_id=rec_id,
            type=rec_type
        ).save()
