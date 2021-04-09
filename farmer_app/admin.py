from django.contrib import admin
from .models import *
from multilingual_model.admin import TranslationStackedInline


class BookTranslationInline(TranslationStackedInline):
    model = BookTranslation


class BookAdmin(admin.ModelAdmin):
    list_display = ["ISBN"]
    inlines = [BookTranslationInline]


# Register your models here.
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Book, BookAdmin)
admin.site.register(Question)