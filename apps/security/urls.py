from django.urls import path
from .views import (SigninView,)

app_name = 'security'

urls = [
    path('signin/', SigninView.as_view(), name='signin'),
]

api = [
]

urlpatterns = urls + api
