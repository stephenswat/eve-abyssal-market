from django.contrib import admin

from eve_mail_queue.models import MailSender, Mail


admin.site.register(MailSender)
admin.site.register(Mail)
