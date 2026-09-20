from django.test import SimpleTestCase, override_settings
from django.urls import reverse
from .content import PROJECTS

@override_settings(STORAGES={'default': {'BACKEND': 'django.core.files.storage.FileSystemStorage'}, 'staticfiles': {'BACKEND': 'django.contrib.staticfiles.storage.StaticFilesStorage'}})
class PortfolioTests(SimpleTestCase):
    def test_home_and_project_navigation(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        for project in PROJECTS:
            url = reverse('project', args=[project['slug']])
            self.assertContains(response, url)
            detail = self.client.get(url)
            self.assertContains(detail, project['name'])
        self.assertContains(response, 'https://github.com/AhmedMurshid')

    def test_unknown_project_is_not_found(self):
        self.assertEqual(self.client.get('/projects/does-not-exist/').status_code, 404)

    def test_resume_download_is_pdf(self):
        response = self.client.get(reverse('resume'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Type'], 'application/pdf')
        self.assertIn('attachment;', response['Content-Disposition'])
        self.assertTrue(b''.join(response.streaming_content).startswith(b'%PDF'))
