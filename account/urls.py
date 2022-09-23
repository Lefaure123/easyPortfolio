from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('', views.akey, name='akey'),
    path('kreyekont/', views.kreyeKont, name='kreyekont'),
    path('konekte/', views.konekte, name='konekte'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
