from typing import List
from django.shortcuts import get_object_or_404
from ninja import NinjaAPI
from .models import *
from .schema import *

api = NinjaAPI()


@api.get("home/")
def home(request):
    return {"text": "Hello World"}


@api.post("inventory/caegory")
def post_category(request, data: CateGorySchema):
    qs = Category.objects.create(**data.dict())
    return {"id": qs.name}


@api.post("inventory/product")
def post_product(request, data: ProductSchema):
    print(data)
    qs = Product.objects.create(
        name=data.name, web_id=data.web_id, category_id=data.category
    )
    return {"name": qs.name}


@api.get("inventory/category/all/", response=List[CateGoryListSchema])
def get_categories(request):
    qs = Category.objects.all()
    return qs


@api.get("inventory/products/all/", response=List[ProductListSchema])
def get_Products(request):
    qs = Product.objects.all()
    return qs


@api.get("inventory/product/category/{category_slug}", response=List[ProductSchema])
def get_product_by_category(request, category_slug):
    qs = Product.objects.filter(category__slug__icontains=category_slug)
    return qs


@api.put("inventory/category/{category_id}")
def update_category(request, category_id: int, data: CateGorySchema):
    category_object = get_object_or_404(Category, id=category_id)
    for attr, value in data.dict().items():
        if value:
            setattr(category_object, attr, value)
    category_object.save()
    return {"Success": True}
