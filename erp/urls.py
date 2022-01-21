from django.urls import path
from erp.views import test_url_view

urlpatterns = [
    path('one/', test_url_view),
    path('two/', test_url_view),
]
