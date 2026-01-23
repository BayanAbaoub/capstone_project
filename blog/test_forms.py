from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .forms import CommentForm
from .models import Review


class TestCommentForm(TestCase):

    def setUp(self):
        """Create test user and review"""
        self.user = User.objects.create_user(
            username="myUsername",
            password="myPassword",
            email="test@test.com"
        )
        self.review = Review.objects.create(
            title="Movie Review Title", 
            author=self.user,
            slug="movie-review-title", 
            excerpt="Movie review excerpt",
            content="Movie review content", 
            status=1
        )

    def test_form_is_valid(self):
        comment_form = CommentForm({'body': 'This is a great review'})
        self.assertTrue(comment_form.is_valid())

    def test_form_is_invalid(self):
        comment_form = CommentForm({'body': ''})
        self.assertFalse(comment_form.is_valid(), msg="Form is valid")
    
    def test_successful_comment_submission(self):
        """Test for posting a comment on a review"""
        self.client.login(
            username="myUsername", password="myPassword")
        review_data = {
            'body': 'This is a test comment.'
        }
        response = self.client.post(reverse(
            'review_detail', args=['movie-review-title']), review_data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(
            b'Comment submitted and awaiting approval',
            response.content
        )