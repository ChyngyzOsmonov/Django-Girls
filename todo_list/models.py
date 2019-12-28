from django.db import models


class ToDoList(models.Model):
    title = models.CharField(max_length=150, db_index=True)
    date_pub = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-date_pub']


