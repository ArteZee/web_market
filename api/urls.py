from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from api import routers

app_name = "api"

urlpatterns = [
    path("auth/", obtain_auth_token,name= "api-token"),
    *routers.category_router.urls,
    *routers.product_router.urls,
    *routers.user_router.urls,
    *routers.order_router.urls,
]