from django.db import models


# Create your models here.

class Node(models.Model):
    name = models.CharField(max_length=100)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    # parent = parent_id.name

    def __str__(self):
        return self.name
