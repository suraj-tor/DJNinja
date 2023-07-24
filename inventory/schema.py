from ninja import Schema, ModelSchema
from .models import *


class CateGorySchema(ModelSchema):
    class Config:
        model = Category
        model_fields = ["name", 'slug']
