from django.urls import path
from django.conf.urls import url, include
from products import views
from rest_framework_swagger.views import get_swagger_view

app_name = 'products'

urlpatterns = [
    path('', views.ProductList.as_view()),
    path('<int:pk>/', views.ProductDetail.as_view()),
    path('api/doc', get_swagger_view(title='Rest API Document')),
]
