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