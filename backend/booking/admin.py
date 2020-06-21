from django.contrib import admin

# Register your models here.
from backend.booking.models import Review


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    pass
