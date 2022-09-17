from django.db import models


# ========== class-to-generate-contact-table ==========

class contact(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name
