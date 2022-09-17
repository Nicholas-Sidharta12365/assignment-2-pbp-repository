from django.test import TestCase, override_settings
from django.test.client import RequestFactory
from .views import mywatchlist

# Create your tests here.
@override_settings(STATICFILES_STORAGE='django.contrib.staticfiles.storage.StaticFilesStorage')
class Sendhelp(TestCase):

    def setUp(self) -> None:
        self.factory = RequestFactory()
        return super().setUp()

    def test_html(self):
        request = self.factory.get("/mywatchlist/html")
        response = mywatchlist(request)
        self.assertEqual(response.status_code, 200)

    def test_xml(self):
        request = self.factory.get("/mywatchlist/xml")
        response = mywatchlist(request)
        self.assertEqual(response.status_code, 200)

    def test_json(self):
        request = self.factory.get("/mywatchlist/json")
        response = mywatchlist(request)
        self.assertEqual(response.status_code, 200)