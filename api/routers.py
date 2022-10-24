from rest_framework import routers

from api import views


app_name = "api"

product_router = routers.SimpleRouter()
category_router = routers.SimpleRouter()
user_router = routers.SimpleRouter()
order_router = routers.SimpleRouter()

product_router.register("product",views.ProductViewSet, basename= "product")
category_router.register("category",views.CategoryViewSet, basename= "category" )

__all__=["product_router", "category_router"]