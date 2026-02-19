from django.db import models


class Genra(models.Model):
    name = models.CharField(max_length=50 , null= False)

    def __str__(self):
        return self.name


class Mission (models.Model):
    name = models.CharField(max_length=50 , null= False)
    description = models.TextField()
    deadline = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_achieve = models.BooleanField()
    genra = models.ForeignKey(Genra , on_delete= models.CASCADE , default='')

    def __str__(self):
        return self.name

