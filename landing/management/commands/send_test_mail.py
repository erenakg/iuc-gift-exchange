from django.core.management.base import BaseCommand
from django.core.mail import send_mail
from django.conf import settings
import logging
import traceback

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = 'Send a test email to the provided address (default: altan.tari@ogr.iuc.edu.tr)'

    def add_arguments(self, parser):
        parser.add_argument('--email', type=str, default='altan.tari@ogr.iuc.edu.tr', help='Recipient email')

    def handle(self, *args, **options):
        to_email = options['email']
        subject = 'Test'
        message = 'Bu bir test e-postasıdır.'
        from_email = settings.DEFAULT_FROM_EMAIL

        self.stdout.write(f'Sending test mail from {from_email} to {to_email} using backend {settings.EMAIL_BACKEND}')

        try:
            result = send_mail(subject, message, from_email, [to_email], fail_silently=False)
            self.stdout.write(self.style.SUCCESS(f'Mail send result: {result}'))
        except Exception as e:
            logger.error('Test mail send failed: %s', e, exc_info=True)
            self.stderr.write(self.style.ERROR('Exception during send_mail:'))
            traceback.print_exc()