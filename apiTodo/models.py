from django.db import models


class Todo(models.Model):
    task = models.CharField(max_length=50)
    description = models.TextField()

    TITLE = (
    ('H', 'High'),
    ('M', 'Medium'),
    ('L', 'Low'),
    )

    priority = models.CharField(max_length=50, choices = TITLE)
    done = models.BooleanField(default=False)
    createdDate = models.DateTimeField(auto_now_add=True)
    updatedDate = models.DateTimeField(auto_now=True)
    finish_date = models.DateTimeField()


    def __str__(self):
        return self.task