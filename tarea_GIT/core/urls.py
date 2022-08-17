from django.conf import settings
from django.urls import path
from . import views

urlpatterns = [
    path('', views.base, name='base'),
    path('hijo', views.hijo, name='hijo')

]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)