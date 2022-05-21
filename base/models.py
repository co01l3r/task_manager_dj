from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    """
    create model which is represented as a database table, use attributes as model columns.
    In this case create table with user, title, description, complete. Django User model handles
    the authentication.

    atr
    ---
    user = one-to-many, when deleted user deletes all children(tasks) as well
    title = string, max length specified, empty not allowed
    description = string, empty allowed
    complete = bool, default value False
    created = string, timestamp when children(task) been created
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=300)
    description = models.TextField(null=True, blank=True)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """
        table representation, returns as string title
        """
        return self.title

    class Meta:
        """
        custom metadata option

        atr
        ---
        ordering = by column
        """
        ordering = ['complete']
