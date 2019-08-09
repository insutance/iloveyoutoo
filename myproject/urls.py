from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from .views import UserCreateView, UserCreateDoneTV, HomeView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),

    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/register/', UserCreateView.as_view(), name='register'),
    path('accounts/register/done/', UserCreateDoneTV.as_view(), name='register_done'),
    path('post/', include('photo.urls')),
    path('freeboard/', include('freeboard.urls')),
    path('showme/', include('showme.urls')),
    path('produce/', include('produce.urls')),
]  + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
