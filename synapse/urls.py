from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.conf.urls.static import static
# from apps.security.views import (CustomLoginView, SignUp, SocialAuth, success_auth,)

urls = [
    path('', include('apps.core.urls', namespace='core')),
    path('synapse-admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

auth = [
    path('accounts/', include('allauth.urls')),
]

third = [
    path('webpush/', include('webpush.urls'))
]

urlpatterns = urls + auth + third
