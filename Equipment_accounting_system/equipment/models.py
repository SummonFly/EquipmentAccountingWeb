from django.db import models


class Equipment(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=[('available', 'Available'), ('in_use', 'In Use'), ('maintenance', 'Maintenance')])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
