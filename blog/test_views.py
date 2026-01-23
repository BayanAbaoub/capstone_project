from django.contrib.auth.models import User
from django.urls import reverse
from django.test import TestCase
from .forms import CommentForm
from .models import Review

class TestBlogViews(TestCase):

    def setUp(self):
        self.user = User.objects.create_superuser(
            username="myUsername",
            password="myPassword",
            email="test@test.com"
        )
        self.review = Review(
            title="Movie Review Title", 
            author=self.user,
            slug="movie-review-title", 
            excerpt="Movie review excerpt",
            content="Movie review content", 
            status=1
        )
        self.review.save()

    def test_render_review_detail_page_with_comment_form(self):
        response = self.client.get(reverse(
            'review_detail', args=['movie-review-title']))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Movie Review Title", response.content)
        self.assertIn(b"Movie review content", response.content)
        self.assertIsInstance(
            response.context['comment_form'], CommentForm)