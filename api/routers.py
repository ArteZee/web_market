from rest_framework import routers

from api import views


app_name = "api"

product_router = routers.SimpleRouter()
category_router = routers.SimpleRouter()
user_router = routers.SimpleRouter()
order_router = routers.SimpleRouter()

product_router.register("product",views.ProductViewSet, basename= "product")
category_router.register("category",views.CategoryViewSet, basename= "category" )
user_router.register("user", views.UserViewSet,basename="user")

__all__=["product_router", "category_router","user_router"]