from django.test import TestCase
from django.core.exceptions import ValidationError
from django.utils.html import escape

import pytest

from lists.models import Item, List


class ListAndItemModelsTest(TestCase):

    @pytest.mark.django_db
    def test_saving_and_retrieving_items(self):
        list_ = List()
        list_.save()

        first_item = Item()
        first_item.text = 'The first (ever) list item'
        first_item.list = list_
        first_item.save()

        second_item = Item()
        second_item.text = 'Item the second'
        second_item.list = list_
        second_item.save()

        saved_list = List.objects.first()
        self.assertEqual(saved_list, list_)

        saved_items = Item.objects.all()
        assert saved_items.count() == 2

        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]

        assert first_saved_item.text == 'The first (ever) list item'
        assert first_saved_item.list == list_
        assert second_saved_item.text == 'Item the second'
        assert second_saved_item.list == list_

    def test_cannot_save_empty_list_items(self):
        list_ = List.objects.create()
        item = Item(list=list_, text='')
        with self.assertRaises(ValidationError):
            item.save()
            item.full_clean()

    def test_validatoin_errors_are_sent_back_to_home_page_template(self):
        response = self.client.post('/lists/new', data={'item_text': ''})
        assert response.status_code == 200
        self.assertTemplateUsed(response, 'home.html')
        expected_error = escape("You can't have an empty list item")

        self.assertContains(response, expected_error)
