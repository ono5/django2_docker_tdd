from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest
from django.template.loader import render_to_string

from lists.views import home_page


class HomePageTest(TestCase):
    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        assert found.func == home_page

    def test_user_home_template(self):
        response = self.client.get('/')
        # template_list = []
        # template_list += [template.name for template in response.templates]
        #
        # assert 'home.html' in template_list

        self.assertTemplateUsed(response, 'home.html')

    def test_can_save_a_POST_request(self):
        response = self.client.post('/', data={'item_text': 'A new list item'})
        assert 'A new list item' in response.content.decode()
        self.assertTemplateUsed(response, 'home.html')
