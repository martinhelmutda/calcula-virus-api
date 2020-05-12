"""calculavirus URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import include, path
from rest_framework import routers
from calculavirus.insumos import views as insumo_views
from calculavirus.checklist import views as checklist_views
from django.contrib import admin
from django.conf import settings
from django.views.static import serve
from django.conf.urls import url

router = routers.DefaultRouter()
router.register(r'users', insumo_views.UserViewSet)
router.register(r'groups', insumo_views.GroupViewSet)
router.register(r'insumos', insumo_views.InsumoViewSet)
router.register(r'lugares', insumo_views.LugarCompraViewSet)
router.register(r'checklist',checklist_views.ChecklistViewSet)
router.register(r'checklistinsumo',checklist_views.ChecklistInsumoViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', serve, {
        'document_root': settings.MEDIA_ROOT,
        }),
    ]
