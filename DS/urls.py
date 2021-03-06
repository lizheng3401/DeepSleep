"""DS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from rest_framework import routers
# from rest_framework.authtoken import views
from rest_framework_jwt.views import obtain_jwt_token
from django.views.static import serve

from .settings import MEDIA_ROOT
from account.views import UserViewSet
from device.views import DeviceViewSet
from sleep.views import SleepViewSet,ReportViewSet
from api.views import SleepRecordViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'devices', DeviceViewSet)
router.register(r'sleeps', SleepViewSet)
router.register(r'reports', ReportViewSet)
router.register(r'sleepRecords', SleepRecordViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls')),
    url(r'^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),
    # url(r'^api-token-auth', views.obtain_auth_token),
    url(r'^login/', obtain_jwt_token),
    url(r'', include(router.urls)),
    url(r'^api/', include('api.urls'))
]
