from django.db import models


# Create your models here.
class Submit(models.Model):
    title = models.CharField(max_length=200)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()

    def __str__(self):
        return self.title
    
class SubmitRequest(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    submission = models.TextField()
    read = models.BooleanField(default=False)

    def __str__(self):
        return f"Submission request from {self.name}"