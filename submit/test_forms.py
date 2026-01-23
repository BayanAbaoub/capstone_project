from django.test import TestCase
from .forms import SubmitForm


class TestSubmitForm(TestCase):

    def test_form_is_valid(self):
        """ Test for all fields"""
        form = SubmitForm({
            'name': 'Test User',
            'email': 'test@test.com',
            'submission': 'Hello!'
        })
        self.assertTrue(form.is_valid(), msg="Form is not valid")