from django.db.models import Q

from huey import crontab
from huey.contrib.djhuey import db_periodic_task

from eve_mail_queue.models import Mail, MailSender
from eve_esi import ESI


@db_periodic_task(crontab(minute='*'))
def send_enqueued_mails():
    for m in MailSender.objects.all():
        client = m.character.get_client()

        while True:
            mails = (
                Mail.objects
                .filter(Q(sender__isnull=True) | Q(sender=m))
                .order_by('-priority', 'created')
            )

            if not mails.exists():
                break

            mail = mails[0]

            req = ESI.request(
                'post_characters_character_id_mail',
                client=client,
                character_id=m.character.character_id,
                mail={
                    "approved_cost": 0,
                    "body": mail.body,
                    "recipients": [
                        r.as_recipient_dict() for r in mail.recipients.all()
                    ],
                    "subject": mail.subject
                }
            )

            if req.status == 201:
                mail.delete()
            else:
                break
