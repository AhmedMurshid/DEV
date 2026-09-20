"""Render Django pages into a portable, static preview. The source remains Django."""
from pathlib import Path
import shutil
from django.conf import settings
from django.core.management.base import BaseCommand
from django.test import Client
from portfolio.content import PROJECTS

class Command(BaseCommand):
    help = 'Export the portfolio to dist/ for static hosting.'

    def handle(self, *args, **options):
        destination = settings.BASE_DIR / 'dist'
        destination.mkdir(exist_ok=True)
        client = Client()
        routes = ['/'] + [f"/projects/{p['slug']}/" for p in PROJECTS]
        for route in routes:
            response = client.get(route)
            if response.status_code != 200:
                raise RuntimeError(f'Cannot export {route}: {response.status_code}')
            target = destination / route.strip('/') / 'index.html'
            target.parent.mkdir(parents=True, exist_ok=True)
            html = response.content.decode().replace('href="/resume/"', 'href="/static/Ahmed_Abdullahi_Resume.pdf" download')
            target.write_text(html, encoding='utf-8')
        shutil.copytree(settings.BASE_DIR / 'static', destination / 'static', dirs_exist_ok=True)
        self.stdout.write(self.style.SUCCESS(f'Exported {len(routes)} pages to {destination}'))
