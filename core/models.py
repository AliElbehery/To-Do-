from django.db import models

class Mission (models.Model):
    name = models.CharField(max_length=50 , null= False)
    description = models.TextField()
    deadline = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_achieve = models.BooleanField()

    def __str__(self):
        return self.name
