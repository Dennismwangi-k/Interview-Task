from django.db import models

class ClosestPoints(models.Model):
    points_string = models.TextField()
    closest_pair = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Points: {self.points_string} - Closest: {self.closest_pair}"
