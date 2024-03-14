from django.db import models

class QBook(models.Model):
    user = models.CharField(max_length=100)
    user_question = models.CharField(max_length=500)

    def __str__(self):
        return self.user

class FAQ(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()


    def __str__(self):
        return self.question