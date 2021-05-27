from django.conf.urls import url
from myapp import views
from rest_framework.routers import DefaultRouter
from .views import ProfileViewSet
from django.urls import include, path

router = DefaultRouter()
router.register(r'update', ProfileViewSet)

app_name = 'dappx'

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^register/$', views.register, name='register'),
    url(r'^user_login/$', views.user_login, name='user_login'),
]
