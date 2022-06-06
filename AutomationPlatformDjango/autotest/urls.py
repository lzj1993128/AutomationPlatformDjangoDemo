from django.urls import path, include
from rest_framework.routers import DefaultRouter

from autotest.views.autotest.autotest import *

router = DefaultRouter()
router.register('Books', BooksViewSet)
router.register('Role', RoleViewSet)
urlpatterns = [
    path('', include(router.urls)),
]
