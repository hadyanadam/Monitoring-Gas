from django.urls import path
from .views import PostPage, UpdatePostPage, AjaxGasView

app_name='api'
urlpatterns = [
    path('ajax/<str:no_tiang>', AjaxGasView.as_view(), name='ajaxgasview'),
    path('', PostPage.as_view(), name='postpage'),
    path('<int:pk>', UpdatePostPage.as_view(), name='updatepostpage')
]
