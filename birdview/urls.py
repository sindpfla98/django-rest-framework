from django.contrib import admin
from django.urls import path, include
from products import views
from rest_framework import routers

urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', include('products.urls')),

]