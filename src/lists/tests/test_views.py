from django.test import TestCase

import pytest

from lists.models import Item, List


class HomePageTest(TestCase):

    def test_user_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

    def test_only_saves_items_when_necessary(self):
        self.client.get('/')
        assert Item.objects.count() == 0

