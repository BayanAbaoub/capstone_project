from django.test import TestCase
from django.urls import reverse
from .models import Submit
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

    def setUp(self):
        """Creates submit page content"""
        self.submit_content = Submit(
            title="Submit a Review", 
            content="Share your movie reviews with us!"
        )
        self.submit_content.save()

    def test_render_submit_page_with_submit_form(self):
        """Verifies get request for submit page containing a submit form"""
        response = self.client.get(reverse('submit'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Submit a Review', response.content)
        self.assertIsInstance(
            response.context['submit_form'], SubmitForm)