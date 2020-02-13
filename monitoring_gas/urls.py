from django.contrib import admin
from django.urls import path,include
from .views import homeView, logView

urlpatterns = [
    path('log/', logView, name='log'),
    path('post_page/', include('api.urls')),
    path('', homeView, name='home'),
    path('admin/', admin.site.urls),
]
