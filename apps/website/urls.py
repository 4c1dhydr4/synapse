from django.urls import path
from django.contrib.auth.decorators import login_not_required
from django.contrib.admin.views.decorators import staff_member_required
from .views import (IndexView,)

app_name = 'website'

urls = [
    path('', login_not_required(IndexView.as_view()), name='index'),
]

api = [
]

urlpatterns = urls + api
