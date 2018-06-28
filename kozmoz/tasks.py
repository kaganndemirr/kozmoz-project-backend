# Django
from django.conf import settings
from django.core.mail import send_mail
from django.urls import reverse
from django.template.loader import render_to_string
from django.utils.translation import ugettext_lazy as _

# Local Django
from kozmoz import celery_app
from posts.models import Post, Comment

@celery_app.task
def mail_task(context, verb):
    """
    Context Format
        context = {
            subject="subject"
            message="messages"
            html_message=render_to_string('email/email.html', template_context),
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[email]
        }
    """

    try:
        send_mail(**context)

        return ','.join(context['recipient_list']) + ' success = ' + verb
    except:
        return ','.join(context['recipient_list']) + ' error = ' + verb
