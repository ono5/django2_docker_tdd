from django.urls import resolve
from django.test import TestCase

from lists.views import home_page
from lists.models import Item

import pytest


class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        assert found.func == home_page

    def test_user_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

    def test_can_save_a_POST_request(self):
        response = self.client.post('/', data={'item_text': 'A new list item'})

        assert Item.objects.count() == 1
        new_item = Item.objects.first()
        assert new_item.text == 'A new list item'

    def test_redirects_after_POST(self):
        response = self.client.post('/', data={'item_text': 'A new list item'})

        assert response.status_code == 302
        assert response['location'] == '/'

    def test_only_saves_items_when_necessary(self):
        self.client.get('/')
        assert Item.objects.count() == 0

    def test_displays_all_list_items(self):
        Item.objects.create(text='itemey 1')
        Item.objects.create(text='itemey 2')

        response = self.client.get('/')

        assert 'itemey 1' in response.content.decode()
        assert 'itemey 2' in response.content.decode()


class ItemModelTest():

    @pytest.mark.django_db
    def test_saving_and_retrieving_items(self):
        first_item = Item()
        first_item.text = 'The first (ever) list item'
        first_item.save()

        second_item = Item()
        second_item.text = 'Item the second'
        second_item.save()

        saved_items = Item.objects.all()
        assert saved_items.count() == 2

        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]

        assert first_saved_item.text == 'The first (ever) list item'
        assert second_saved_item.text == 'Item the second'
