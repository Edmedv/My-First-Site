from django.urls import path

from mainapp.views import first_page, create_product



urlpatterns = [
    path('', first_page, name='home'),
    path('create/', create_product, name='create'),
]

