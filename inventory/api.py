from ninja import NinjaAPI
from .models import *
from .schema import *

api = NinjaAPI()

@api.get("home/")
def home(request):
    return {"text":"Hello World"}


@api.post("inventory/caegory")
def post_category(request, data:CateGorySchema):
    qs = Category.objects.create(**data.dict())
    return {"id":qs.name}

@api.post('inventory/product')
def post_product(request, data:ProductSchema):
    print(data)
    qs = Product.objects.create(name=data.name, web_id=data.web_id, category_id=data.category)
    return {'name':qs.name}