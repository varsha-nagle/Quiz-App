from django.urls import path
from .views import index, login_view

urlpatterns = [
    path('', index, name='index'),
    path('login/',login_view, name="login")
    # other urlpatterns
]