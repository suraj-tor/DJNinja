from ninja import Schema, ModelSchema
from .models import *


class CateGorySchema(ModelSchema):
    class Config:
        model = Category
        model_fields = ["name", "slug"]


class CateGoryListSchema(ModelSchema):
    class Config:
        model = Category
        model_fields = ["id", "name", 'slug']


class ProductSchema(ModelSchema):
    class Config:
        model = Product
        model_fields = ["name", "web_id", "category"]


class ProductListSchema(ModelSchema):
    class Config:
        model = Product
        model_fields = "__all__"