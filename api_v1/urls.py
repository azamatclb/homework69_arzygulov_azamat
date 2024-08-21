from django.urls import path

from api_v1.views import add, subtract, multiply, divide, get_csrf_token

app_name = 'api_v1'

urlpatterns = [
    path("get_csrf/", get_csrf_token),
    path('add/', add),
    path('subtract/', subtract),
    path('multiply/', multiply),
    path('divide/', divide),
]
