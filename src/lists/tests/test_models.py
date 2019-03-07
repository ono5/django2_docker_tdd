from django.test import TestCase
from django.core.exceptions import ValidationError
from django.utils.html import escape

import pytest

from lists.models import Item, List


class ListAndItemModelsTest(TestCase):

    def test_cannot_save_empty_list_items(self):
        list_ = List.objects.create()
        item = Item(list=list_, text='')
        with self.assertRaises(ValidationError):
            item.save()
            item.full_clean()

    def test_validatoin_errors_are_sent_back_to_home_page_template(self):
        response = self.client.post('/lists/new', data={'text': ''})
        assert response.status_code == 200
        self.assertTemplateUsed(response, 'home.html')
        expected_error = escape("You can't have an empty list item")

        self.assertContains(response, expected_error)

    def test_get_absolute_url(self):
        list_ = List.objects.create()
        assert list_.get_absolute_url() == f'/lists/{list_.id}/'

    def test_duplicate_items_are_invalid(self):
        list_ = List.objects.create()
        Item.objects.create(list=list_, text='bla')
        with self.assertRaises(ValidationError):
            item = Item(list=list_, text='bla')
            item.full_clean()

    def test_CAN_asve_same_item_to_different_list(self):
        list1 = List.objects.create()
        list2 = List.objects.create()
        Item.objects.create(list=list1, text='bla')
        item = Item(list=list2, text='bla')
        item.full_clean() # should not raise

    def test_list_ordering(self):
        list1 = List.objects.create()
        item1 = Item.objects.create(list=list1, text='i1')
        item2 = Item.objects.create(list=list1, text='item 2')
        item3 = Item.objects.create(list=list1, text='3')
        assert list(Item.objects.all()) == [item1, item2, item3]

    def test_string_representation(self):
        item = Item(text='some text')
        assert str(item) == 'some text'


class ItemModelTest(TestCase):

    @pytest.mark.django_db
    def test_default_text(self):
        item = Item()
        self.assertEqual( item.text, '' )


class ListModelTest(TestCase):

    def test_item_is_related_to_list(self):
        list_ = List.objects.create()
        item = Item()
        item.list = list_
        item.save()
        assert item in list_.item_set.all()
