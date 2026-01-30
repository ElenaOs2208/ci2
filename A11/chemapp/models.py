from django.db import models


class SmilesSearch(models.Model):
    smiles = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.smiles} ({self.created_at})"

