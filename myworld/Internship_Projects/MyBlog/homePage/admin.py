from django.contrib import admin
from .models import user, articles, book
# Register your models here.
admin.site.register(user)
admin.site.register(articles)
admin.site.register(book)
