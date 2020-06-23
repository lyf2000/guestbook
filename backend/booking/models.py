from django.db import models

# Create your models here.


# TODO validators


class Review(models.Model):
    author_name = models.CharField(max_length=32)
    text = models.CharField(max_length=512)

    created_at = models.DateTimeField(auto_now_add=True)
    # TODO ImageField
    # image = models.ImageField()

    class Meta:
        ordering = ('-created_at', )
