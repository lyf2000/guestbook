from django.core.exceptions import ValidationError
from django.db import models

# Create your models here.


# TODO validators

def validate_name(value):
    if len(value) < 5:
        raise ValidationError(u'Too short')


class Review(models.Model):
    author_name = models.CharField(max_length=32)
    text = models.CharField(max_length=512)

    created_at = models.DateTimeField(auto_now_add=True)
    # TODO ImageField
    image = models.ImageField(upload_to='uploads/reviews/%Y/%m/%d/', null=True, blank=True)

    class Meta:
        ordering = ('-created_at', )

    # def save(self, *args, **kwargs):
    #     validate_name(self.author_name)
    #     super().save(*args, **kwargs)