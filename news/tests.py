from django.test import TestCase
from django.urls import reverse
from .models import model1

# Create your tests here.
class NewsModelTest(TestCase):
    def setUp(self):
        model1.objects.create(title='News1', text='Yangilik matni1')

    def test_content(self):
        news1 = model1.objects.get(id=1)
        object_title = f'{news1.title}'
        object_text = f'{news1.text}'
        self.assertEqual(object_title,'News1')
        self.assertEqual(object_text, 'Yangilik matni1')

class newsViewTest(TestCase):
    def setUp(self):
        model1.objects.create(title='News2', text='Yangilik matni2')

    def test_proper_location(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code,200)

    def test_url_name(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code,200)

    def test_template(self):
        resp = self.client.get(reverse('home'))
        self.assertTemplateUsed(resp,'home.html')
