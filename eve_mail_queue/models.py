from django.db import models

from eve_auth.models import EveUser


class MailSender(models.Model):
    character = models.ForeignKey(EveUser, models.CASCADE)


class Mail(models.Model):
    sender = models.ForeignKey(MailSender, models.SET_NULL, null=True)

    subject = models.CharField(max_length=80)
    body = models.TextField()

    created = models.DateTimeField(auto_now_add=True)
    priority = models.IntegerField(default=0)


class MailRecipient(models.Model):
    TYPE_CHARACTER = 0
    TYPE_CORPORATION = 1
    TYPE_ALLIANCE = 2

    TYPE_CHOICES = (
        (TYPE_CHARACTER, "Character"),
        (TYPE_CORPORATION, "Corporation"),
        (TYPE_ALLIANCE, "Alliance"),
    )

    mail = models.ForeignKey(Mail, models.CASCADE, related_name="recipients")
    recipient_id = models.BigIntegerField()
    type = models.SmallIntegerField(choices=TYPE_CHOICES)

    def as_recipient_dict(self):
        return {"recipient_id": self.recipient_id, "recipient_type": self._type_str()}

    def _type_str(self):
        if self.type == self.TYPE_CHARACTER:
            return "character"
        elif self.type == self.TYPE_CORPORATION:
            return "corporation"
        elif self.type == self.TYPE_ALLIANCE:
            return "alliance"
