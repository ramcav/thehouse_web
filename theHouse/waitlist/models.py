from django.db import models

class UserSubmission(models.Model):
    email = models.EmailField()
    username = models.CharField(max_length=100)
    date_submitted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username