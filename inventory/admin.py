from django.contrib import admin
from .models import Category, Product, Media


# Register your models here.
def getFieldsModel(model):
    fields = [
        field.name
        for field in model._meta.get_fields()
        if field.many_to_many != True and field.one_to_many != True
    ]
    return fields


class CategoryAdmin(admin.ModelAdmin):
    list_display = getFieldsModel(Category)


class ProuctAdmin(admin.ModelAdmin):
    list_display = getFieldsModel(Product)


class MediaAdmin(admin.ModelAdmin):
    list_display = getFieldsModel(Media)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProuctAdmin)
admin.site.register(Media, MediaAdmin)
