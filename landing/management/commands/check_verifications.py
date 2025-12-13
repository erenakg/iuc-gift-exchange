from django.core.management.base import BaseCommand
from django.conf import settings
from landing.models import EmailVerification
from pathlib import Path


class Command(BaseCommand):
    help = 'Given an email, prints EmailVerification records and tails django-error.log'

    def add_arguments(self, parser):
        parser.add_argument('email', type=str, help='Email to check')
        parser.add_argument('--lines', type=int, default=200, help='Number of log lines to show')

    def handle(self, *args, **options):
        email = options['email']
        lines = options['lines']

        self.stdout.write(f'Checking verifications for: {email}')

        qs = EmailVerification.objects.filter(user__email=email).order_by('-created_at')
        if not qs.exists():
            self.stdout.write(self.style.WARNING('No EmailVerification records found.'))
        else:
            self.stdout.write(self.style.SUCCESS(f'Found {qs.count()} records:'))
            for ev in qs:
                self.stdout.write(
                    f'- code={ev.code} created_at={ev.created_at} expires_at={ev.expires_at} is_used={ev.is_used} ip={ev.ip_address}'
                )

        # Tail log
        base = getattr(settings, 'BASE_DIR', None)
        if not base:
            self.stdout.write(self.style.WARNING('BASE_DIR not set in settings; cannot find django-error.log'))
            return

        log_path = Path(base) / 'django-error.log'
        if not log_path.exists():
            self.stdout.write(self.style.WARNING(f'Log file not found: {log_path}'))
            return

        self.stdout.write('\n--- Log tail: %s (last %s lines) ---\n' % (log_path, lines))
        with log_path.open('r', encoding='utf-8', errors='ignore') as f:
            all_lines = f.readlines()
            for l in all_lines[-lines:]:
                self.stdout.write(l.rstrip())
