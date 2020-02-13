from django.urls import path
from .views import PostPage, UpdatePostPage

app_name='api'
urlpatterns = [
    path('', PostPage.as_view(), name='postpage'),
    path('<int:pk>', UpdatePostPage.as_view(), name='updatepostpage')
]
