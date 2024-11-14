from django.urls import path

from mainapp.views import first_page, create_product, personal_account


urlpatterns = [
    path('', first_page, name='home'),
    path('create/', create_product, name='create'),
    path('person/', personal_account, name='personal_account'),
]

