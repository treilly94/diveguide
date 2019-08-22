from django.test import TestCase
from django.urls import reverse

from .models import Location


def create_divesite(**kwargs):
    return Location.objects.create(**kwargs)


class IndexViewTests(TestCase):

    def test_index_page_empty(self):
        url = reverse('divesites:index')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'divesites/index.html')
        self.assertContains(response, 'Fresh water sites')
        self.assertContains(response, 'Salt water sites')

    def test_index_page_sw(self):
        kwargs = {"location_name": "Trefor Pier",
                  "water_type": "SW"}
        site = create_divesite(**kwargs)
        url = reverse('divesites:detail', args=(site.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'divesites/detail.html')
        self.assertContains(response, site.location_name)


class DetailViewTests(TestCase):

    def test_detail_page(self):
        kwargs = {"location_name": "Trefor Pier"}
        site = create_divesite(**kwargs)
        url = reverse('divesites:detail', args=(site.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'divesites/detail.html')
        self.assertContains(response, site.location_name)
