from django.urls import path
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from .views import (IndexView,)

app_name = 'core'

urls = [
    path('', IndexView.as_view(), name='index'),
    # path('', login_required(IndexView.as_view()), name='index'),
]

api = [
]

urlpatterns = urls + api
